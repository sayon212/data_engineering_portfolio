#########################################################################################################
# Import Libraries 
#########################################################################################################
import gradio as gr
import json
from databricks.vector_search.client import VectorSearchClient
from openai import OpenAI
from tavily import TavilyClient
import brevo_python
from brevo_python.rest import ApiException
from typing import Dict

#########################################################################################################
# embeddings - convert user question to embeddings and fetch using RAG
#########################################################################################################
def generate_embeddings(text):
    client = OpenAI(
                api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                base_url="https://dbc-xxxxxx-ea61.cloud.databricks.com/serving-endpoints"
                )
    response = client.embeddings.create(
                model='databricks-gte-large-en',
                input=text
                )
    return response

#########################################################################################################
# rag retriever
#########################################################################################################
def rag_retriever(query_vector):
    vsc = VectorSearchClient(
    workspace_url="https://dbc-xxxxxxxx-ea61.cloud.databricks.com",
    personal_access_token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    )
    index = vsc.get_index(endpoint_name="best_practices_db", index_name="workspace.llm_dev.idx_resume_qa")
    results = index.similarity_search(query_vector=query_vector, columns="chunk", num_results=3)
    return results['result']['data_array']

#########################################################################################################
# tool to send email
#########################################################################################################
def send_email(subject: str, html_body: str):
    config = brevo_python.configuration.Configuration()
    config.api_key['api-key'] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(config))

    send_smtp_mail = brevo_python.SendSmtpEmail(
        sender = {"name":"Sayon" , "email":"xxxxxx@gmail.com"},
        to = [{"email":"xxxxxx@gmail.com" , "name": "Sayon"}] , 
        subject = subject,
        html_content = html_body
    )
    response = api_instance.send_transac_email(send_smtp_mail)
    return {"recorded": "ok"}

send_email_json = {
    "name" : "send_email",
    "description" : "Always use this tool to send email",
    "parameters": {
        "type": "object",
        "properties": {
            "subject": {
                "type": "string",
                "description": "The email subject"
            },
            "html_body": {
                "type": "string",
                "description": "The email body"
            },
        },
        "required": ["subject","html_body"],
        "additionalProperties": False
    }
}    

tools = [{"type": "function", "function": send_email_json}]

def handle_tool_calls(tool_calls):
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        print(f"Tool called: {tool_name}", flush=True)

        if tool_name == "send_email":
            result = send_email(**arguments)

        results.append({"role": "tool","content": json.dumps(result),"tool_call_id": tool_call.id})
    return results


#########################################################################################################
# instructions
#########################################################################################################
name = "Sayon"

system_prompt = f"""You are acting as {name}. You are answering questions on {name}'s LinkedIn profile,
particularly questions related to {name}'s career, background, skills and experience.
Your responsibility is to represent {name} for interactions on the website as faithfully as possible.
Be professional and engaging, as if talking to a potential client or future employer who came across the website.
If you don't know the answer to any question tell you dont know clearly.
You are equipped with send_email tool to send mail to Sayon.
If a user requests to get in touch with a specific message then only you 
should use the send_email tool by creating a subject and use the user question as it is in email message body.
"""

#########################################################################################################
# LLM
#########################################################################################################

def chat(question):
    query_vector = generate_embeddings(question).data[0].embedding
    context = rag_retriever(query_vector)

    client = OpenAI(
                api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                base_url="https://dbc-xxxxx-ea61.cloud.databricks.com/serving-endpoints"
                )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Question: {question}\n\nContext from knowledge base:\n{context}"}
    ]

    response = client.chat.completions.create(
            messages=messages,
            model="databricks-meta-llama-3-3-70b-instruct",
            max_tokens=256, tools = tools
            )
    
    finish_reason = response.choices[0].finish_reason
    if finish_reason=="tool_calls":
        message = response.choices[0].message
        tool_calls = message.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(results)
    else:
        done = True

    return response.choices[0].message.content

#########################################################################################################
# Gradio UI
#########################################################################################################
with gr.Blocks(css="""
    body { background-color: #f0f4f8; }
    .gr-button { background-color: #4CAF50; color: white; font-weight: bold; }
    .gr-textbox { border-radius: 8px; }
""") as demo:

    gr.Markdown("<h1 style='text-align:center; color:#4CAF50;'>💬 My Professional Experience Bot</h1>")
    gr.Markdown("<p style='text-align:center; color:#555;'>Ask me about my career!</p>")

    with gr.Row():
        question_input = gr.Textbox(
            label="Your Question:",
            placeholder="Type your question here...",
            lines=2,
        )
        ask_button = gr.Button("🚀 Ask")

    answer_output = gr.Textbox(
        label="Answer:",
        placeholder="The answer will appear here...",
        lines=4,
    )

    ask_button.click(chat, inputs=question_input, outputs=answer_output)
#########################################################################################################

if __name__ == "__main__":
    demo.launch()
