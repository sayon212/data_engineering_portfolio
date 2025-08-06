# 🛒 Serverless Order Management System (Azure Microservices)

A scalable, event-driven **order management platform** built using **Azure Functions**, **Cosmos DB**, **Service Bus**, and **Azure Web Apps** — designed for modern eCommerce scenarios with clean separation of concerns via microservices.

---

## 🚀 Key Features

- 📦 Event-driven microservices handling order lifecycle  
- ☁️ 100% Serverless with Azure Functions
- 💾 Cosmos DB for flexible, low-latency storage  
- 📬 Asynchronous processing using Azure Service Bus  
- 🌐 User-friendly frontend hosted on Azure Web App  
- ✉️ Email notification using Azure Communication Services

---

## 🧠 Architecture Overview
<img width="1249" height="762" alt="image" src="https://github.com/user-attachments/assets/1f9a92b3-4b9e-470c-b6ff-9f61735557df" />



---

## 🧰 Tech Stack & Azure Services

| Component              | Purpose                                                                 |
|------------------------|-------------------------------------------------------------------------|
| **Azure Functions**    | Serverless compute for each microservice (independent, scalable logic)  |
| **Azure Service Bus**  | Reliable, asynchronous message delivery between services                |
| **Cosmos DB**          | NoSQL database for orders, invoices, and inventory                      |
| **Azure Web App**      | Hosts the frontend  application                                         |
| **Azure Communucation Services** | Email Notification                                            |

---

## 🎯 Why These Choices?

- **Azure Functions**: Pay-per-use, auto-scale microservices. Each business logic like `create_order`, `validate_payment`, etc. runs independently.
- **Service Bus**: Enables **decoupled communication** across services, allowing retries, failure handling, and parallel processing.
- **Cosmos DB**: NoSQL, globally distributed, great for **order/inventory data** with dynamic schemas.
- **Azure Web App**: Quick deployment for lightweight frontends with full integration to backend APIs.

---

## 📁 Folder Structure for Azure function

```
Azure-microservices/
├── create_order/                        # Handles order creation
├── validate_payment/                    # Validates payment status
├── submit_order/                        # Submits order after validation
├── update_inventory_generate_invoice/   # Updates inventory & creates invoice
├── dispatch_notification/               # Sends shipment/dispatch notification
├── email_service/                       # Sends confirmation/failure emails
│
├── host.json                            # Azure Functions host config
├── local.settings.json                  # Local dev environment settings
└── requirements.txt                     # Python package dependencies
```
---
## 📁 Folder Structure for Azure Web App

```
WebApp/
├── app.py                        # python flask app          
├── templates/                    # html pages
│  ├── landing.html               # landing page
│  ├── shopping.html              # when user clicks shopping button
│  ├── register.html              # when user clicks register
└── requirements.txt          
```

---
## Process flow:

👤 **User places an order**

⚡ **Flask App: Validates customer**
   - 🗃️ Checks if customer exists  
   - 📩 If not, registers and stores in Customer_master (Cosmos DB)

⚡ **Azure Function: submit_order (HTTP trigger)**
   - 📩 Sends message to orders Service Bus  

⚡ **Azure Function: create_order (Service Bus trigger)**  
   - 🔄 Creates order in Cosmos DB with payment/shipment/dispatch = pending  
   - 📩 Forwards payment info to payment Service Bus  

⚡ **Azure Function: validate_payment**  
   - 🔄 Validates if (qty × price) == user-entered payment  
   - 📩 Sends confirmation to invoice_inventory Service Bus  

⚡ **Azure Function: confirm_payment**  
   - 💳 Updates payment status in Cosmos DB  
   - 📩 Sends message to next stage via Service Bus  

⚡ **Azure Function: update_inventory_generate_invoice**  
   - 📦 Updates stock in Cosmos DB & marks invoice status  
   - 🧾 Generates fake invoice  
   - 📩 Sends message to dispatch Service Bus  

⚡ **Azure Function: dispatch_order**  
   - 🚚 Adds shipping info & delivery ETA to Cosmos DB  
   - 📦 Generates fake shipping ID, delivery date  
   - 📩 Sends message to email_service Service Bus  

⚡ **Azure Function: notify_customer**  
   - 📧 Sends email via Azure Communication Services  
   - ✅ Marks order as 'Completed' in CosmosDB

---

## Setup Instructions
- **Clone the repository**
- **Get Azure subscription free trial or pay as you go**

  
## Setting Up Cosmos DB
- **Create Azure Cosmos NoSQL Service with a database and following containers like this:**

<img width="619" height="450" alt="image" src="https://github.com/user-attachments/assets/68d6f4b1-6d78-450d-a76f-5db4cb5fc20b" />

- **Create dummy record in product_master**

<img width="589" height="191" alt="image" src="https://github.com/user-attachments/assets/fb5637f4-7dbf-4387-94d6-8ceaf725baf2" />

- **Create dummy record in inventory_master**

<img width="583" height="217" alt="image" src="https://github.com/user-attachments/assets/56db7901-35ae-4620-aa0d-15ac3e0d827c" />

---

## Setting Up Azure Communication Services(ACS)
- Create ACS resource from azure portal
- Open the resource and create email domain
<img width="1230" height="542" alt="image" src="https://github.com/user-attachments/assets/f6b7b40b-d8f3-403a-9543-980bc0801464" />

- Copy the domain name. It will be used as environment variable in the Azure function


## Setting Up Azure Functions
- Create Azure function service from portal with minimum plan capacity
- Open VSCode from the Azure-microservices/ root folder in local machine
- Install Azure functions extensions and Azure tools from Vscode and Azure icon will be visible
- Login from VScode in azure
- Here will be the folder strucure
<img width="437" height="443" alt="image" src="https://github.com/user-attachments/assets/9cf28b64-65f5-4e80-a6b6-bd7cd95b1f06" />

- Shift + Ctrl + P -> Deploy to Azure function. Select the azure function app and deploy
- On Successful deployment all the azure functions will be visible from portal
<img width="1021" height="564" alt="image" src="https://github.com/user-attachments/assets/ede2d74c-b5a5-4df7-af62-4a38ca1b6bb3" />

- Click Start from the Function portal to start the function
  
**Adding environment variables (very important)**
- Navigate to the following location and add last 4 variables in function app
- Go to cosmos and service bus settings the keys and connection strings are available
- Use the ACS domain name from last step and store inside environment variable SENDER_ADDRESS

<img width="604" height="517" alt="image" src="https://github.com/user-attachments/assets/2e8d27b6-bbfc-421b-9442-dd038e53b674" />


---

## Setting Up Service Bus
- From azure portal create service bus. Inside it create 5 queues like this:

<img width="1063" height="451" alt="image" src="https://github.com/user-attachments/assets/62b911a2-eb48-4985-af3d-9f5448495844" />

- Service Bus setup done!

---

## Setting up the WebApp
- From azure portal create Web App service with Windows/Linux host machine minimum capacity / free capacity.
- Start the app
  
**Adding environment variables (very important)**
- Navigate to the following location and add these variables in function app

<img width="637" height="474" alt="image" src="https://github.com/user-attachments/assets/3819ad9e-2dd6-4d75-af09-18da1bd204fd" />

- Now go the the WebApp folder in local machine and open VSCode from that root

<img width="964" height="583" alt="image" src="https://github.com/user-attachments/assets/b2811a44-9d5c-4dfe-9a62-7067c5ce99f3" />

- Ensure Azure tools is installed in VSCode extension
- Ensure the folder structure
- Shift + Ctrl + P -> Deploy to Azure App. Select the azure app and deploy
- Go to the App service in portal and start the app and click browse icon just next to the start button to open the WebPage.
- If deployment is successful the webpage will Open like this using Azure domain

<img width="1022" height="572" alt="image" src="https://github.com/user-attachments/assets/cea98e45-118d-4a91-b3eb-d08114de0791" />

---

## Test the App
- First register a user
- The go to shopping and add name, email, amount
- Amount is taken as input from user on purpose since I have not added payment gateway
- So if payment amount and user input amount does not match then its a failed case scenario.
- For a positive test scenario enter the correcr amount and Click Submit
<img width="1222" height="466" alt="image" src="https://github.com/user-attachments/assets/99a11a84-8a3f-45f7-9434-53d2587fd12e" />

**Place order and click Submit**
- Go to the service bus Queue and we see the messages are moving to and from the Queues triggering one after another
- Cosmos DB being continuously updated at the same time
  
## Queue movement
- Orders
<img width="605" height="190" alt="image" src="https://github.com/user-attachments/assets/2e9afaa4-6839-4eab-b2e2-81a54ba6cde3" />

- Invoice
<img width="598" height="268" alt="image" src="https://github.com/user-attachments/assets/717be84d-10ff-4ace-b968-654fbe5ffee9" />

- Dispatch
<img width="679" height="239" alt="image" src="https://github.com/user-attachments/assets/f651193f-9515-4b38-ad7f-6501662eddfd" />

- Email queue
<img width="707" height="263" alt="image" src="https://github.com/user-attachments/assets/03731c57-ac22-4c55-9a60-608e8e2822ac" />

## Cosmos DB collections
- Orders
<img width="543" height="314" alt="image" src="https://github.com/user-attachments/assets/a734b726-6901-4928-8741-7d1242025600" />

- Payments Validation
<img width="562" height="223" alt="image" src="https://github.com/user-attachments/assets/1567b946-dae1-4126-9471-408f0fcc15e8" />

- Invoice and Shipment
<img width="553" height="228" alt="image" src="https://github.com/user-attachments/assets/c7d22d09-9571-4681-8514-2b7a00fe4e05" />

## Email Notification
<img width="1027" height="253" alt="image" src="https://github.com/user-attachments/assets/08d859f6-1e07-4545-8649-fae03d62cc6f" />

---

## 🧠 Learning Outcomes

✅ Real-world use of serverless event-driven architecture  
✅ Hands-on experience with multiple Azure components  
✅ Microservice design with decoupled services  
✅ Deployment-ready serverless project  

---

## 🧠 Short Note
This is a learning project. This is not perfect like what happens in large ecommerce. I tried to simulate some scenarios and learn
Service Bus, Cosmos DB, Azure functions etc. There are lot of scope to improve this. I put more stress on backend function here
to learn about serverless event driven framework. Clone this and you are most welcome for improvemt solutions and make it way better.
Thank you for your time and patience!

## 👨‍💻 **About the Author**
I am Sayon Bhattacharjee, a passionate engineer with expertise in building scalable and modern enterprise solutions using multicloud and diverse range of Big Data technologies.
I love solving real-world data challenges, optimizing workflows, and exploring cutting-edge tools to deliver high-quality, production-ready solutions.

🔗 [LinkedIn](https://www.linkedin.com/in/sayon-bhattacharjee-a33380218/)

---

> ⭐ *Feel free to fork or star this repo if you found it useful! Pull requests and improvements welcome.*
