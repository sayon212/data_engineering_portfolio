from backend.core import run_llm
import streamlit as st

# Streamlit UI
st.title("Document Chatbot")
st.write("Ask me anything!")

# Chat input
user_input = st.text_input("You:", "")

if "question_history" not in st.session_state:
    st.session_state["question_history"] = []

if "answer_history" not in st.session_state:
    st.session_state["answer_history"] = []

# Button to submit the question
if st.button("Send"):
    if user_input.strip() != "":
        with st.spinner("Generating response..."):
            response = run_llm(user_input)
            st.text_area("Bot:", value=response, height=500)

            st.session_state["question_history"].append(user_input)
            st.session_state["answer_history"].append(response)

        if st.session_state["answer_history"]:
            for response, user_input in zip(st.session_state["answer_history"], st.session_state["question_history"]):
                st.chat_message("user").write(user_input)
                st.chat_message("assistant").write(response)
    else:
        st.warning("Please enter a question.")





