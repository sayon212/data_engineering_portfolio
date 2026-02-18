# 🚀 Lakeflow | Spark Declarative Pipeline (SDP)

A modern Spark Declarative Pipeline (Delta Live Tables) for incremental ingestion, CDC handling, SCD Type 2, and fact aggregation — all without writing complex MERGE logic.

This project highlights how Spark Declarative Pipelines abstract away boilerplate code and allow engineers to focus on business logic.

# 🧠 What I learned

✅ Auto Loader (Incremental File Ingestion)

✅ Streaming Tables

✅ Auto CDC Flow

✅ SCD Type 2

✅ Materialized Views

✅ Declarative framework

# 🏗️ Architecture Overview

<img width="1120" height="300" alt="image" src="https://github.com/user-attachments/assets/47c834b5-1bdf-4b36-9836-6e4b05379d64" />


```
Landing
   │
   ├── Customer Data ──▶ Auto Loader ──▶ Streaming Table ──▶ SCD Type 2 Table
   │
   └── Transaction Data ──▶ Auto Loader ──▶ Streaming Table ──▶ Fact Table
                                                           │
                                                           ▼
                                               Customer Sales Aggregation
```

# 📦 Datasets
## 👤 Customer Dataset

Contains updates over time - name, phone, email

Requires historical tracking (SCD Type 2)

# 💳 Transaction Dataset

## Customer transactions

Append-only data

Used to build the fact table

# 🔄 Data Ingestion (Auto Loader)

Both datasets are ingested from the landing zone

Uses Spark Auto Loader for:

Incremental file detection

Schema inference & evolution

Scalable streaming ingestion

# 🕒 Customer SCD Type 2 (Auto CDC Flow)

Customer streaming data is processed using Auto CDC Flow

SCD Type 2 handled declaratively

SDP automatically manages:

Row versioning

🚫 No manual MERGE statements

🚫 No complex change detection logic

✅ Clean

✅ Reliable

✅ Production-ready

# 📊 Transaction Fact Table

Ingested via Auto Loader

Stored as a streaming table

Loaded into a Materialized View (append-only)

This forms the Fact Transactions Table optimized for analytics.

# 🔗 Final Aggregation

Fact table is LEFT JOINED with the customer SCD table

Computes:

💰 Total sales per customer

🧮 Customer-level aggregations

# ✨ Why Spark Declarative Pipelines?

🚀 Minimal code

🧩 Built-in best practices

🛠️ Automatic dependency management

📈 Scales effortlessly

🧠 Lets engineers focus on logic, not infrastructure

This project shows how complex patterns like SCD Type 2 become trivial using declarative pipelines.

# 🧩 Schema Evolution & Pipeline Resilience

One of the most powerful benefits I observed while building this project was how schema changes propagate automatically across the entire pipeline.

✨ What This Means in Practice

🔁 Rename any table

🏷️ Rename any column

➕ Add new columns

➖ Remove existing columns

🔄 Change data types

🧪 Modify transformation logic

➡️ All downstream tables automatically adapt

➡️ No manual fixes, no broken dependencies

# ✨ Flexible Target Schema

With the newer Spark Declarative Pipeline capabilities:

✅ Streaming tables can be created in any schema

✅ Materialized views can live in any schema

✅ Pipelines are no longer locked to a single namespace

✅ Easier alignment with domain-driven data design

## 👨‍💻 **About the Author**
I am Sayon Bhattacharjee, a passionate Data Engineer with expertise in building scalable and modern data pipelines using multicloud and diverse range of Big Data technologies.
I love solving real-world data challenges, optimizing workflows, and exploring cutting-edge tools to deliver high-quality, production-ready solutions.

🔗 [LinkedIn](https://www.linkedin.com/in/sayon-bhattacharjee-a33380218/)
