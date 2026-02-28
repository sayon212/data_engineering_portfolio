# 📊 Partitioning vs Liquid Clustering in Databricks

This repository contains a Databricks notebook that evaluates Delta table partitioning versus Liquid Clustering (CLUSTER BY AUTO), with a focus on file scanning behavior and query performance.

## 🧪 Experiment Summary

## The notebook demonstrates how different table layouts affect:
- Number of data files created
- File pruning during query execution
- Query runtime when access patterns change
- Synthetic data is used to ensure a controlled and reproducible setup.

## 🔹 Step 1: Data Creation
- Fake dataset generated for analysis
- Includes a date column suitable for partitioning

## 🔹 Step 2: Writing Data with Partitioning
- Data written using:
- PARTITION BY date

## 📌 Observed outcome:
- Creation of hundreds of small files
- Increased file fragmentation

## 🔹 Step 3: Query Using Partition Column
- Point lookup query filtered on the partition column (date)

## ✅ Databricks Query Profiler results:
- 1 file scanned
- Effective partition pruning
- Low query latency

## 🔹 Step 4: Query Using Non-Partition Columns
- Query modified to filter on a different set of columns

<img width="538" height="399" alt="image" src="https://github.com/user-attachments/assets/080d6a39-139b-4d3e-8d86-8de79374c6a4" />

## ⚠️ Observed behavior:
- ~250 files scanned
- Significant file open/close overhead
- Query runtime approximately 7 seconds
- 📌 This highlights the limitation of static partitioning when query patterns change.

# 🔁 Liquid Clustering Approach

## 🔹 Step 5: Rewrite Table Without Partitioning
- Table rewritten without PARTITION BY
- Enabled CLUSTER BY AUTO (Liquid Clustering)

## 🔹 Step 6: Optimize Table
- OPTIMIZE command executed to reorganize data layout

## 🔹 Step 7: Re-execute the Query
- Same query from Step 4 executed again

## 🚀 Results:
- 1 file scanned
- Query runtime approximately 1 second
- Reduced file access overhead

<img width="438" height="372" alt="image" src="https://github.com/user-attachments/assets/29dbc826-c119-41c3-8732-cd5db55056a7" />

## 📈 Comparison Summary

Partitioned Table
-----------------
• File Count        : High (many small files)

• Query Adaptability: Low (dependent on partition columns)

• File Pruning      : Works only on partition filters

• Query Runtime     : ~7 seconds (non-partition predicates)

Liquid Clustering
-----------------
• File Count        : Optimized and compact

• Query Adaptability: High (adapts to access patterns)

• File Pruning      : Pattern-based and dynamic

• Query Runtime     : ~1 second

## ✅ Key Observations
- Partitioning performs well only when queries consistently use partition columns.
- Changing query predicates can significantly increase file scans.
- Liquid Clustering adapts to query access patterns and mitigates the small file problem.
- Optimized clustering results in fewer files and faster query execution.
