# 🚀Building an Idempotent Data Ingestion Pipeline in Databricks
This project shows how I built an incremental ingestion pipeline using Databricks Auto Loader, hit a real production problem, and then fixed it by design.
It’s a story of what went wrong, why it went wrong, and how I solved it 🛠️

## 🧩 The Problem

In real data platforms:

📂 Files can be re-sent

🔄 Jobs can be re-run

❌ Bad data can land in production tables

⏪ Tables may need rollback / restore

The big question:

Can I safely re-run my pipeline without duplicating data?

## 🧪 Part 1: Auto Loader
What I Built First

- I started with a basic Auto Loader pipeline:
- Incremental CSV ingestion from a landing zone
- Structured Streaming
- Delta Lake target
- Schema evolution using rescue mode
- Checkpoint-based state tracking

## ✨ Result:
- Only new files are processed
- Restarting the job works fine
- Exactly-once semantics (as long as state exists)

## ⚠️ Important Observation
- When I deleted the checkpoint directory…
- 💥 Auto Loader reprocessed all files in the landing zone
- This is not a bug. This is how Auto Loader is designed.
- 👉 Idempotency here is checkpoint-dependent.
- Auto Loader guarantees incremental ingestion, not absolute idempotency.

## 🔥 Part 2: Damage Control: Fix data in target table
- Some bad records made it into the target Delta table 😬
- ⏪ Restored the Delta table using time travel to latest correct version

## 🧠 Part 3: Idempotency by Design
### 💡 The Design Decision
- I decided to own idempotency explicitly.
- Use file_name as a unique ingestion key
- Enforce idempotency using MERGE
- One file = one ingestion event
- This was intentional and simple.

### ⚙️ Implementation: foreachBatch + MERGE
- 🚚 Read incrementally using Auto Loader
- 📦 Process data in micro-batches (foreachBatch)
- 🔀 MERGE into Delta table
- 🔑 Match on file_name

## ✅ What This Solved
- 🎉 Now the pipeline supports:
- Safe re-runs after checkpoint deletion
- Safe reprocessing after table restore
- No duplicate ingestion
- Clear audit trail of ingested files

## 📌 What I learned
- ✅ Auto Loader in its simplest form
- ❌ What breaks during recovery
- ❌ Checkpoint can corrupt due to any reason in logic change
- ⏪ Delta table restore in action
- ⚠️ Why append-only pipelines fail
- 🧠 How to design idempotency explicitly







