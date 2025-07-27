# 🚀 Crypto Data Engineering Pipeline (Python + Postgres + dbt + Airflow + Docker)

## **Overview**
This project is an **end-to-end data engineering pipeline** that ingests cryptocurrency data from the **CoinGecko API**, loads it into a **PostgreSQL `raw` schema**, transforms it into `curated` and `processed` layers using **dbt**, and prepares **reporting views** for **Power BI**.  
The entire workflow is orchestrated using **Apache Airflow** and runs seamlessly inside **Docker containers**.

---

## **Architecture**
![Architecture](powerBi/architecture_diagram.png)

## **🛠 Tech Stack**
- 🐍 **Python** – Data ingestion from CoinGecko API  
- 🌬 **Apache Airflow** – Workflow orchestration  
- 🧱 **dbt** – SQL-based transformations and testing  
- 🗄 **PostgreSQL** – Data warehouse with layered schemas  
- 🐳 **Docker & docker-compose** – Containerized setup  
- 📊 **Power BI** – Reporting and dashboards  

## **✨ Features**
- 🔄 Automated data ingestion pipeline using Airflow DAGs.  
- 🏗 **Layered architecture:** raw → curated → processed → report.  
- 🧪 **dbt** for transformations, tests, and documentation.  
- ⭐ **Star schema** with dim and fact tables in the processed schema.  
- 📈 Reporting views ready for Power BI in the report schema.  
- 🐳 Fully containerized and reproducible using Docker Compose.  

## **📂 Project Structure**
```bash
project-crypto-dbt-airflow/
├── airflow-dags/             
│   └── airflow_pipeline.py     # airflow pipeline
├── dbt_crypto_project/
│   ├── models/                 # dbt transformatio logic
│   │   ├── curated/
│   │   ├── processed/
│   │   └── reporting/
│   └── dbt_project.yml
├── scripts/
│   ├── ingest_crypto_data.py   # python ingestion
├── powerBi                     # dashboard sample
├── docker-compose.yml
├── Dockerfile
├── Dockerfile.airflow          # configuire airflow with dbt and libraries
├── requirements.txt
└── README.md
```
⚡ Setup Instructions
1. Clone the repository
2. Setup Docker in local machine
3. Inside the local folder that contains the project and docker files run docker build commands

```bash
docker compose up     #containers up -d
docker ps             #containers should be visible

#initialise the dbt project
docker-compose run airflow airflow db init
 
# create profiles.yml
docker-compose run airflow airflow users create --username airflow --password airflow --firstname Data --lastname Engineer --role Admin --email data@engineer.com
```

This will start:

🗄 PostgreSQL

🌬 Airflow Webserver & Scheduler

🧱 dbt container

## **Access Services**
🌐 Airflow UI: http://localhost:8080

🗄 PostgreSQL: localhost:5432

## **Check Airflow**
Open port at localhost:8080 from browser Airflow should be visible.
<img width="831" height="431" alt="image" src="https://github.com/user-attachments/assets/057fa652-674c-418d-837c-43c28a7d8c16" />

## **Trigger the DAG**
The DAG should complete with 2 tasks Python and DBT
<img width="731" height="505" alt="image" src="https://github.com/user-attachments/assets/a9710340-51df-40c5-896e-4948129aa6e4" />

## **Verify data from postgres**
I have connected to postgres from DBeaver
- **host**: localhost:5432
- **user**: airflow
- **password**: airflow
<img width="1091" height="699" alt="image" src="https://github.com/user-attachments/assets/aa6179e0-68a3-40e7-a5fd-7a12e110d450" />

## **Star Schema**
<img width="805" height="563" alt="image" src="https://github.com/user-attachments/assets/591504ba-7fdf-4117-b0a1-fc5078a5bb0f" />

## **Simple PowerBI report**
<img width="859" height="481" alt="image" src="https://github.com/user-attachments/assets/9543ff05-c681-4977-9751-6acf1708a850" />

## **Common errors**
1. **Logs folder error**: give permission
```bash
rmdir /s /q .\dbt_crypto_project\logs
mkdir .\dbt_crypto_project\logs
icacls .\dbt_crypto_project\logs /grant Everyone:F /T
```
2. **Target folder error**: give permission
```bash
docker exec -it airflow bash    #verify container name
rm -rf /opt/dbt/target
mkdir -p /opt/dbt/target
chmod -R 777 /opt/dbt/target
```

## 👨‍💻 **About the Author**
I am Sayon Bhattacharjee, a passionate Data Engineer with expertise in building scalable and modern data pipelines using multicloud and diverse range of Big Data technologies.
I love solving real-world data challenges, optimizing workflows, and exploring cutting-edge tools to deliver high-quality, production-ready solutions.

🔗 [LinkedIn](https://www.linkedin.com/in/sayon-bhattacharjee-a33380218/)
