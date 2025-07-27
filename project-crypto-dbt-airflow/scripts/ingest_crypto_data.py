#!/usr/bin/env python
import pandas as pd, requests, os, time
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv(dotenv_path='/opt/scripts/.env')
API_KEY = os.getenv("API_KEY")
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DB   = os.getenv("PG_DB")

def get_engine():
    conn_url = f"postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}"
    return create_engine(conn_url, pool_pre_ping=True)

def ensure_schema(engine, schema: str):
    with engine.begin() as conn:
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema};"))

def load_df_to_postgres(df: pd.DataFrame, engine,table, schema, mode):
    df.to_sql( table, engine, schema = schema, if_exists = mode, index = False, chunksize = 500, method="multi")        

def get_coin_market_data():
    retry = 5
    try:
        for i in range(retry):
            limit = 10
            url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page={limit}&page=1&sparkline=false&price_change_percentage=1h,24h,7d"
            headers = {"accept": "application/json"}
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                time.sleep(20)
                print('Sleeping....')
                continue
            return response.json()
    except:
        print("All retries exhausted.")


def get_coin_data_by_id(coin_id, days):
    retry = 5
    for i in range(retry):
        try:
            vs_currency = "usd"
            url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency={vs_currency}&days={days}"
            response = requests.get(url, headers={"accept": "application/json"})
            if response.status_code != 200:
                print(f"coin id: {coin_id}")
                print('Sleeping.....')
                time.sleep(20)
                continue
            return response
        except:
            print(f"All retries exhausted. Skipping coin {coin_id}")
    
def get_coin_hist_data(coin_df):
    all_hist_data = []
    for coin_id in coin_df['id']:
        response = get_coin_data_by_id(coin_id=coin_id, days=5)
        coin_hist_data = response.json()
        df_prices = pd.DataFrame(coin_hist_data["prices"], columns=["timestamp", "price"])
        df_mcap = pd.DataFrame(coin_hist_data["market_caps"], columns=["timestamp", "market_cap"])
        df_vol = pd.DataFrame(coin_hist_data["total_volumes"], columns=["timestamp", "total_volumes"])
        df_merge = df_prices.merge(df_mcap,on='timestamp').merge(df_vol,on='timestamp')
        df_merge['timestamp'] = pd.to_datetime(df_merge['timestamp'], unit='ms')
        df_merge['coin_id'] = coin_id
        all_hist_data.append(df_merge[["coin_id","price","market_cap","total_volumes","timestamp"]])
    return all_hist_data


def run_pipeline():
    engine = get_engine()
    ensure_schema(engine,'raw')
    market_metrics = get_coin_market_data()
    df_market_metrics = pd.json_normalize(data=market_metrics)
    load_df_to_postgres(df_market_metrics, engine, 'market_metrics', 'raw', 'replace')
    print(f"Loaded {len(df_market_metrics)} rows into market_metrics table")

    all_hist_data_combined = get_coin_hist_data(df_market_metrics)
    hist_df = pd.concat(all_hist_data_combined)
    load_df_to_postgres(hist_df, engine, 'coin_historical', 'raw', 'replace')
    print(f"Loaded {len(hist_df)} rows into coin_historical table")

  
if __name__ == "__main__":
    run_pipeline()
