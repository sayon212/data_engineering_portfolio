# 🚀 Azure DIY Spark in Azure Virtual Machines Cluster (in 5 Minutes!)

[![Azure](https://img.shields.io/badge/Azure-Cloud-blue?logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)
[![Spark](https://img.shields.io/badge/Apache%20Spark-3.5.0-orange?logo=apachespark&logoColor=white)](https://spark.apache.org/)
[![Python](https://img.shields.io/badge/Python-3.10-green?logo=python&logoColor=white)](https://www.python.org/)
[![Linux](https://img.shields.io/badge/Linux-Ubuntu-red?logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![Data Engineering](https://img.shields.io/badge/Data%20Engineering-Building-success)](#)

**Create my own managed Spark cluster** on Azure VMs—quick, hands-on, and cloud-first.  
Perfect as a learning exercise or portfolio project to demonstrate infra, networking, and distributed computing skills.

---


# 🔗 Read my full article which shows step by step setup:
👉 [Read the detailed walkthrough on Medium](https://medium.com/@sayon.biems/i-created-my-own-managed-spark-cluster-within-just-5-minutes-in-azure-80a0614d5453)  

---

##  Why This Project?

- **⚙ Learn Full Stack Setup**  
  From VM provisioning to cluster validation, understand each layer in action—not abstracted by tools like Databricks.

- **⏱ Lightning-Fast Deployment**  
  Build a 3-node Spark cluster (1 master, 2 workers) in about **5 minutes**. Fast, tight, and efficient.

- **🌐 Master Azure Networking**  
  Understand VNets, SSH access, public/private IPs, and firewall rules tailored for Spark workloads.

---

##  Architecture Overview
<img width="640" height="311" alt="image" src="https://github.com/user-attachments/assets/a9d4be74-4aa7-4e3b-b079-24a29ccba6b7" />

---

## 🛠️ Tech Stack
| Component        | Details                                  |
|------------------|------------------------------------------|
| ☁️ Cloud         | Azure Virtual Machines + VNet            |
| 🐧 OS            | Ubuntu                                   |
| ⚡ Compute       | 3 VMs (1 master, 2 workers)              |
| 🔥 Spark         | Apache Spark 3.5.0 (Hadoop 3)            |
| 🐍 Language      | Python (PySpark) + Bash scripts          |
| 📊 Monitoring    | Spark UI (8080 & 4040)                   |


## 📚 What I Learned

- 🖧 **Azure Networking** → VNets, private IPs, firewall rules  
- ⚡ **Cluster Orchestration** → How master & workers connect  
- 🔍 **Spark Internals** → Master-Worker communication & job scheduling  
- 💡 **Why Managed Services Exist** → After doing it manually, Databricks feels magical


## Spark running in Azure VM
<img width="640" height="338" alt="image" src="https://github.com/user-attachments/assets/4f90e19a-9ebc-409e-8de2-df82c233de92" />


## Worker Node in Azure VM
<img width="640" height="573" alt="image" src="https://github.com/user-attachments/assets/31939ef8-6c5c-4ecd-9c4a-b40961acb735" />


## Spark running in Master
<img width="640" height="330" alt="image" src="https://github.com/user-attachments/assets/a75e65f6-1507-4b6a-bbb3-5e7de3b8ac95" />


## 👨‍💻 **About the Author**
I am Sayon Bhattacharjee, a passionate engineer with expertise in building scalable and modern enterprise solutions using multicloud and diverse range of Big Data technologies.
I love solving real-world data challenges, optimizing workflows, and exploring cutting-edge tools to deliver high-quality, production-ready solutions.

🔗 [LinkedIn](https://www.linkedin.com/in/sayon-bhattacharjee-a33380218/)

---

> ⭐ *Feel free to fork or star this repo if you found it useful! Pull requests and improvements welcome.*

