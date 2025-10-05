# 🚀 CareerBot – Personal Career LLM Assistant

CareerBot is an AI-powered bot built on Databricks + LangChain that answers questions about my career, projects, and technical expertise.
It’s recruiter-ready and can notify me via email when someone wants to reach out! 💼✨


## 🛠️ Tech Stack

- Databricks ☁️ – AI & data platform
- Databricks Serving Endpoints 🤖 – LLM
- Python 🐍 – Core logic
- SQL 🗄️ – RAG Knowledge base
- Tavily API ✉️ – Email notifications
- Gradio - Frontend UI

## 🛠️ Key Features

- 🎯 Recruiter can ask anything about my career, skills, and projects
- 📩 Automated email notifications for recruiter queries
- 🔍 Uses RAG for context-aware, accurate answers
- ⚡ Fast and reliable responses

# Setup Instructions
## 1. Get Databricks free edition

## 2. Setup Tavily free account
This will be used to send email. Create API Key

<img width="1200" height="344" alt="image" src="https://github.com/user-attachments/assets/3f89d903-e304-48f5-9cce-37da5a24fa54" />

## 3. Copy the Housekeeping notebook in Databricks workspace
- First create a volume in Databricks workspace and upload your resume.
- Then run cell PRE-REQUISITE STARTS HERE to PRE-REQUISITE END HERE
- Read PDF
- Split into Chunks
- Create table
- Load Chunks into table

## 4. Create Vector Search endpoint

**Go to Databricks compute and create a vector search endpoint**
  
<img width="874" height="580" alt="image" src="https://github.com/user-attachments/assets/7ee19d5e-584e-4a45-9ff1-ba8f9aadbe9a" />

<img width="824" height="292" alt="image" src="https://github.com/user-attachments/assets/955b17d8-79c6-4743-bb5e-6eadf927c31b" />

## 5. Create Vector Search Index on the table pointing to the above endpoint

**From catalog explorer navigate to table. Click create and select Vector search index**

<img width="1037" height="397" alt="image" src="https://github.com/user-attachments/assets/03f8a873-c7a4-4c7b-9297-e265201518c2" />

<img width="677" height="537" alt="image" src="https://github.com/user-attachments/assets/3407dce8-d24f-41f8-bf38-301f9a3c9179" />

<img width="679" height="406" alt="image" src="https://github.com/user-attachments/assets/df9f37cf-eca2-422c-9480-7ea03bee7c2d" />

<img width="673" height="330" alt="image" src="https://github.com/user-attachments/assets/20173e69-56a6-41e4-b911-274d441484de" />

## 6. The table now is storing the embeddings 
**Verify from Catalog explorer**

<img width="1092" height="466" alt="image" src="https://github.com/user-attachments/assets/e44d9812-2d65-4ed7-856e-a7499a72f1b2" />

## 6. Setup is now complete. Now prepare for app.
- Create a new folder in workspace.
- Upload the .py and requirements.txt file
- Replace and verify the access tokens, Tavily key and workspace URLs
- Verify everything in py file

## 7. Create the databricks and point to the folder in step 6

- Go to Databricks compute -> Apps -> Create App -> Create Custom app

<img width="687" height="520" alt="image" src="https://github.com/user-attachments/assets/859f5216-9cfb-41f3-a61c-572e1cb9bd7d" />

<img width="700" height="510" alt="image" src="https://github.com/user-attachments/assets/7271c6b0-44d3-49da-84ac-0942c51a79cf" />

- App will get created.
  
- In the app setting Click deploy. Click deploy with different source code and navigate to the py folder. Click Deploy.

<img width="1329" height="433" alt="image" src="https://github.com/user-attachments/assets/2dd4e835-66c6-4730-970b-46dee3ecbe05" />

## 8. App deployment and verify logs

<img width="690" height="506" alt="image" src="https://github.com/user-attachments/assets/99d6af31-4698-40a1-ace8-69bcce7c1503" />

## 9. Click the deployed URL and open the page

<img width="1242" height="593" alt="image" src="https://github.com/user-attachments/assets/3e71d601-f6b8-491d-910d-ad41cea1545c" />

## 10. Test Email - "I want to reach out to Sayon. My emails is abcd@xyz.com"

<img width="604" height="251" alt="image" src="https://github.com/user-attachments/assets/09a1d2c0-a1b3-4d95-bb3d-960191460bf6" />









