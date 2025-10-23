# 🧠 SQL Server LLM Agent — Intelligent Database Assistant

This project demonstrates an AI-powered SQL Server assistant built using LLM Agents.
It understands natural language queries, automatically generates optimized T-SQL, and executes them safely using built-in tool functions. ⚙️💬

# 🌟 Overview

The SQL Agent acts as a smart layer between the user and SQL Server. It can:

- 🕵️ Understand user intent (query, create, delete, modify, etc.)
- 📊 Fetch metadata to build accurate queries
- 🧠 Generate clean, optimized SQL
- ⚡ Execute DDL/DML/TCL commands only after user confirmation
- 💬 Respond in Gradio-friendly HTML format

# 🧩 Tech Stack
**Component	Description**
- LLM Agent Framework	For orchestrating AI-based tools
- OpenAI Chat Completions Model	Core reasoning and SQL generation
- Python	Execution environment
- Gradio	Interactive frontend (HTML output support)
- SQL Server	Target database for query execution

# ⚙️ How It Works
![image](https://github.com/user-attachments/assets/7340ce35-0d9c-42f2-bc57-e5c47b1454b1)

# 🧰 Tools Used
|**Internal Tools**|**Purpose**|
|------|---------|
|**🧾 get_metadata**|**Fetch metadata (columns, data types, etc.) for a given table**|
|**📈 fetch_data**|**Executes a SELECT query and returns results as an HTML table**|
|**⚙️ execute_sql**|**Executes any DDL/DML/TCL SQL statement safely**|

# 💬 Example Conversation

👤 User:

Show me top 5 employees by salary.

🤖 Agent:

Can you please confirm the schema and table name?

👤 User:

Schema = hr, Table = employees

🤖 Agent Output:

**🧾 Here is the SQL:**
```
SELECT TOP 5 employee_id, first_name, last_name, salary
FROM hr.employees
ORDER BY salary DESC;
```
**🧾 Here is the Data:**
| employee_id | first_name | last_name | salary |
| ----------- | ---------- | --------- | ------ |
| 101         | John       | Doe       | 120000 |
| 205         | Mary       | Smith     | 110000 |
| ...         | ...        | ...       | ...    |

<img width="1254" height="640" alt="image" src="https://github.com/user-attachments/assets/69015799-34bd-4ef5-9290-84f6b099c1b2" />

# 🪄 Features

✅ Understands complex user intent

✅ Generates clean, readable SQL

✅ Fetches live data directly from SQL Server

✅ Handles DDL, DML, and TCL safely

✅ Always confirms before execution

✅ Returns results in rich, HTML format

## 🧠 What I Learned
🔍 LLM & SQL Integration

🧩 Tool-Oriented Agent Design

⚙️ Prompt Engineering

💬 Conversational Workflow

🧠 Model Optimization

🧾 Output Structuring & UI Integration

## 👨‍💻 **About the Author**
I am Sayon Bhattacharjee, a passionate Data Engineer with expertise in building scalable and modern data pipelines using multicloud and diverse range of Big Data technologies.
I love solving real-world data challenges, optimizing workflows, and exploring cutting-edge tools to deliver high-quality, production-ready solutions.

🔗 [LinkedIn](https://www.linkedin.com/in/sayon-bhattacharjee-a33380218/)
