import pandas as pd
import time
import uuid
import json
from azure.eventhub import EventHubProducerClient, EventData

EVENT_HUB_CONNECTION_STR = "USE YOUR CONNECTION STRING"
EVENT_HUB_NAME = "stockshub"

file_paths = [
    "Data/sun_pharma.csv",
    "Data/icici.csv",
    "Data/wipro.csv",
    "Data/hdfclife.csv",
    "Data/reliance.csv"
]

dfs = []
for path in file_paths:
    df = pd.read_csv(path)
    df['trading_time'] = pd.to_datetime(df['trading_time']).dt.strftime("%Y-%m-%dT%H:%M:%S")
    dfs.append(df.iterrows())  # store iterators, not DataFrames

producer = EventHubProducerClient.from_connection_string(
    conn_str=EVENT_HUB_CONNECTION_STR,
    eventhub_name=EVENT_HUB_NAME
)

while True:
    all_empty = True

    for i, iterator in enumerate(dfs):
        try:
            _, row = next(iterator)
            all_empty = False  # At least one file still has data

            message = {
            "event_id": str(uuid.uuid4()),
            "trading_timestamp": row['trading_time'],
            "symbol": row['symbol'],
            "ltp": float(row['ltp']),
            "volume": row['volume'],
            "num_trade": row['num_trades']
            }

            event_data = EventData(json.dumps(message))

            with producer:
                producer.send_batch([event_data])

            print(f"Sent from file {i+1}: {message}")

        except StopIteration:
            # This file is finished
            continue

    if all_empty:
        break  # Exit loop when all files are exhausted

    time.sleep(5)  # Wait before next round

print("All data sent.")
