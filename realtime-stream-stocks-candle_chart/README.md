# 📈 Real-Time Stock Tick Simulation & Candlestick Chart with Azure Event Hub, Stream Analytics, Cosmos DB, PowerBI

## 🚀 Project Overview

This project simulates **real-time stock market ticks** and processes them through **Azure Event Hub → Azure Stream Analytics → Azure Cosmos DB → Power BI**, producing a **live candlestick chart** 📊.

I designed this to showcase **real-time data streaming, transformation, storage, and visualization** skills using **Azure services**.

## 🗂️ Project Architecture

<img width="1007" height="448" alt="image" src="https://github.com/user-attachments/assets/12b47048-0439-403a-8a83-82aeb6daeca4" />

## **📂 Project Structure**
```bash
realtime-stream-stocks-candle-chart/
├── Data/                     # data is purely fake for learning purpose
│   └── hdfclife.csv
│   └── reliance.csv
│   └── sunpharma.csv
│   └── wipro.csv
│   └── icici.csv
├── Python producer/          # data producer to send data to event hub
│   └── producer.py
├── Stream Analytics/         # stream query to process data every 30 second
│   ├── process.sql
├──PowerBI/
│   ├── stocks_streaming.pbix
└── README.md
```

## 🔧 Services & Tools Used
Service / Tool	Purpose
- 🐍 Python	Reads 5 fake stock tick CSV files & sends data to Event Hub every 5 seconds
- ☁️ Azure Event Hub	Ingests streaming tick data in real-time
- ⚡ Azure Stream Analytics	Processes data using tumbling window (30s) to calculate Open, High, Low, Close (OHLC)
- 🌌 Azure Cosmos DB	Stores processed OHLC data for visualization
- 📊 Power BI	Displays a real-time candlestick chart from Cosmos DB

## 📜 Workflow

## 🐍 Python Producer
- Iterates over files and sends tick data to Azure Event Hub every 5 seconds.
- Mimics real market feed.

## ☁️ Azure Event Hub
- Acts as the stream ingestion layer.
- Ensures reliable delivery to downstream processing.

## ⚡ Azure Stream Analytics Job
- Tumbling window of 30 seconds for OHLC calculation:
- Sends aggregated data to Cosmos DB.

## 🌌 Azure Cosmos DB
- Stores OHLC data for each stock every 30s.
- Used as the live data source for Power BI.

## 📊 Power BI
- Connects directly to Cosmos DB.
- Builds a real-time candlestick chart showing price movements.

## Step by step how to setup:

Clone the repo
## From Azure portal setup **Azure Event Hubs** like this

<img width="862" height="542" alt="image" src="https://github.com/user-attachments/assets/026771cb-5b3e-413e-99a7-501d7d536fda" />

## Create **Cosmos DB** database and container like this

<img width="664" height="485" alt="image" src="https://github.com/user-attachments/assets/160bf8b6-8e8c-4aa3-b654-c98703b0bf63" />

## Create a **Stream analytics job** like this and set input (event hub) and output(cosmos db)
Copy and paste the SQL in query section like this

<img width="1359" height="486" alt="image" src="https://github.com/user-attachments/assets/eefe8c3d-7449-4540-b3de-e778ff015368" />

## Setup the python producer in local machine and run the code. It will start sending data to event hub.
Make sure data folder has the data files

<img width="731" height="612" alt="image" src="https://github.com/user-attachments/assets/9a13f130-faa6-418e-a71f-ef944c4f0c42" />

<img width="1128" height="400" alt="image" src="https://github.com/user-attachments/assets/57f6c6f8-b391-4d8c-818b-a96d456f90a5" />

- Open Event hub data explorer to confirm it is sending events
<img width="1168" height="378" alt="image" src="https://github.com/user-attachments/assets/18479deb-b6ed-470f-af20-c522fdfe0b9d" />

- The stream analytics job will immediately process the data and send to cosmos db as 30 second calculated open, high, low close price for every stock
<img width="1074" height="414" alt="image" src="https://github.com/user-attachments/assets/165b4190-13c4-4bba-bd42-cd29898f175a" />

## **Power BI report**
Create a Power BI report . You need to import Candlestick chart pattern power BI visual from internet.

By default candle stick chart is not available. I have downloaded the visual file from web.

Connect Power BI to cosmos DB and create candlestick chart.

Refresh the report to view a beautiful candlestick pattern in realtime.

<img width="1017" height="591" alt="image" src="https://github.com/user-attachments/assets/13f69eea-5cbe-48c5-b9c9-3b0f52d4cbcc" />

## 🎯 Scope of the Project

✅ Simulate real-time market data without relying on paid APIs.

✅ Learn & implement real-time event streaming architecture.

✅ Gain hands-on with Azure streaming ecosystem.

✅ Build live financial dashboards for decision-making.

## 📚 What I Learned

✅ Event Streaming Concepts: Producer, Consumer, Event Hub.

✅ Azure Stream Analytics: Tumbling windows, aggregation queries.

✅ Data storage in Cosmos DB.

✅ Real-Time Visualization: Power BI Direct Query mode for instant updates.

✅ Python & Cloud Integration: Using SDKs to send messages to Event Hub.


## 🧠 Short Note
This is a learning project. Data used here is fake generated and for learning. This was one one my hobby project to silumate
candlestick chart in realtime. I used Azure stack for this project. Same can be achieved using various other tech stacks.
Thank you for your time and patience!


## 👨‍💻 **About the Author**
I am Sayon Bhattacharjee, a passionate Data Engineer with expertise in building scalable and modern data pipelines using multicloud and diverse range of Big Data technologies.
I love solving real-world data challenges, optimizing workflows, and exploring cutting-edge tools to deliver high-quality, production-ready solutions.

🔗 [LinkedIn](https://www.linkedin.com/in/sayon-bhattacharjee-a33380218/)


