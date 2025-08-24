# 🚀 Securing Spark in Azure VM using Bastion

![Azure](https://img.shields.io/badge/Azure-Cloud-blue?logo=microsoft-azure&logoColor=white)
![Azure VM](https://img.shields.io/badge/Azure-VM-0078D4?logo=microsoft-azure&logoColor=white)
![Cloud](https://img.shields.io/badge/Cloud-Computing-1E90FF?logo=icloud&logoColor=white)
![Data Engineering](https://img.shields.io/badge/Data-Engineering-orange?logo=databricks&logoColor=white)
![Bastion](https://img.shields.io/badge/Azure-Bastion-2C7DFA?logo=microsoft-azure&logoColor=white)
![VNet](https://img.shields.io/badge/Azure-VNet-0066B8?logo=microsoft-azure&logoColor=white)
![Networking](https://img.shields.io/badge/Networking-Secure-228B22?logo=cisco&logoColor=white)
[![Linux](https://img.shields.io/badge/Linux-Ubuntu-red?logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![Medium](https://img.shields.io/badge/Blog-Medium-black?logo=medium)](https://medium.com/@sayon.biems)


In this project, I am focusing on the networking and security setup around that cluster. 
I created a dedicated Virtual Network (VNet) with Subnets to logically isolate resources, 
applied Network Security Groups (NSGs) for fine-grained traffic control, and used Azure 
Bastion to connect securely to the VMs without exposing public IPs. With this design, 
my Spark cluster isn’t just functional — it’s protected at an enterprise level.

# 🔗 Read my full article which shows step by step setup:
👉 [Read the detailed walkthrough on Medium](https://medium.com/@sayon.biems/securing-my-apache-spark-cluster-on-azure-with-bastion-849c063e3fec) 


## Architecture
<img width="640" height="252" alt="image" src="https://github.com/user-attachments/assets/a7ff5705-331d-44c6-8146-cb15f154c5ae" />


## 🛠️ Tech Stack

| Component | Description |
|-----------|-------------|
| ☁️ **Azure Cloud** | Core platform for deploying & managing resources |
| 💻 **Azure Virtual Machines (VMs)** | Compute backbone for workloads |
| 🌐 **Azure Virtual Network (VNet)** | Secure private network for communication |
| 🔀 **Subnets** | Logical segmentation inside VNets for isolation & scalability |
| 🔒 **Network Security Groups (NSG)** | Fine-grained inbound/outbound traffic control |
| 🛡️ **Azure Bastion** | Browser-based secure RDP/SSH without exposing public IPs |


## 🌍 Why This Project?
I wanted to go beyond just creating Virtual Machines and Spark clusters. Real-world Data Engineering & Cloud projects demand **secure networking, controlled access, and governance**.  
That’s why I explored **Azure Bastion, VNet, Subnet, and Network Security Groups (NSG)** to understand how large-scale companies secure their cloud environments.  

## 📚 What I Learned
- 🌐 **Virtual Networks (VNet)** – Backbone of Azure networking, isolating workloads securely.  
- 🔀 **Subnets** – Segmentation of networks for better control, performance, and scalability.  
- 🔒 **Network Security Groups (NSG)** – How to allow/block traffic at subnet & NIC level.  
- 🛡️ **Azure Bastion** – Secure, browser-based RDP/SSH without exposing VM IPs to the public internet.  
- 🚪 **Private Access** – Importance of restricting public endpoints and routing via secure gateways.  
- 🏢 **Enterprise Practice** – How cloud companies design for **zero-trust architecture**.  

## ⚡ Why Is This Important?
- 🔑 **Security First** – Most data breaches happen due to misconfigured networks. Learning to secure infra is as important as building it.  
- 🚀 **Industry Standard** – Any enterprise-grade Data Engineering solution must have strong networking & security fundamentals.  
- 🌐 **Cloud-Native Design** – Without VNet, Subnets & NSG knowledge, projects are incomplete.  
- 🏆 **Career Advantage** – Knowing Spark/Data pipelines is good, but **knowing how to secure them on Azure makes you stand out**.  

## Create Bastion
<img width="640" height="555" alt="image" src="https://github.com/user-attachments/assets/aadd5248-24c8-4d87-ace4-f0494e3f1af1" />

## Login with Bastion
<img width="640" height="364" alt="image" src="https://github.com/user-attachments/assets/c11937be-e9ac-40e8-ad36-3ba1ad777611" />

## Connected to Virtual Machine
<img width="640" height="547" alt="image" src="https://github.com/user-attachments/assets/c275787b-3a38-41dc-b053-6f3f8235dba0" />

## ✅ Final Note  

This project was not just about setting up **Azure resources** but about understanding the importance of **secure networking** in the cloud.  

- 🔐 Learned how **VNet, Subnet, NSG, and Bastion** work together to ensure end-to-end security.  
- 🌐 Gained hands-on knowledge of **network isolation, access control, and secure connectivity**.  
- 📚 Reinforced best practices for building **real-world, enterprise-grade cloud architectures**.  

🚀 With this foundation, I am more confident in designing **secure and scalable data engineering solutions** on Azure.


## 👨‍💻 **About the Author**
I am Sayon Bhattacharjee, a passionate engineer with expertise in building scalable and modern enterprise solutions using multicloud and diverse range of Big Data technologies.
I love solving real-world data challenges, optimizing workflows, and exploring cutting-edge tools to deliver high-quality, production-ready solutions.

🔗 [LinkedIn](https://www.linkedin.com/in/sayon-bhattacharjee-a33380218/)







