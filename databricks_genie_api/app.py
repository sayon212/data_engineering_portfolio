import time, requests

genie_space_id = ""
workspace_url = "" 
access_token = "" 
base_url = f"{workspace_url}/api/2.0/genie/spaces/{genie_space_id}"

# start a conversation
def start_conversation(question):
    url = f"{base_url}/start-conversation"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {"content": question}
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    answer = response.json()
    conversation_id = answer['message']['conversation_id']
    message_id = answer['message_id']
    return conversation_id, message_id

# fetch answer using conversation_id, message_id
def fetch_response(conversation_id,message_id):
  url = f"{base_url}/conversations/{conversation_id}/messages/{message_id}"
  headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
  }
  response = requests.get(url,headers=headers)
  response.raise_for_status()
  answer = response.json()
  return answer

# try fetching answer until success status. 
# maximum timeout is 240 seconds. It taskes sometime to start the cluster
def start_polling(conversation_id, message_id, sleep=2, timeout=240):
  start=time.time()
  while True:
    res = fetch_response(conversation_id,message_id)
   
    if res['status'] == 'COMPLETED':
      return res
    
    if time.time()-start > timeout:
      return "No answer from Genie"

    time.sleep(2)  

# parse the answer
def get_answer(payload: dict):
  if payload == "No answer from Genie":
    answer_text = payload
  else:
    attachments = payload.get("attachments", [])
    for att in attachments:
        t = att.get("text", {})
        if isinstance(t, dict) and "content" in t:
          answer_text = t.get("content")
  return answer_text

# How to use
conversation_id, message_id = start_conversation(question='How many records are present in the sales table?')
res = start_polling(conversation_id, message_id)
text_answer = get_answer(res)
print(text_answer)
