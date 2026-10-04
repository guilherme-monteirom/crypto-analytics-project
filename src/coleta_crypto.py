# Projeto Crypto Analytics

import datetime
import requests
import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv

# CONFIGURAÇÕES

load_dotenv()
coingecko_apikey = os.getenv("coingecko_apikey")

# COLETA API

requisicao = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,ripples,cardano,binancecoin&vs_currencies=usd,eur,brl&include_market_cap=true&include_24hr_change=true/x-cg-demo-api-key:{coingecko_apikey}")

df_requisicao = pd.DataFrame(requisicao.json())

# TRANFORMAÇÃO

tickers = {
    "Bitcoin":"BTC",
    "Ethereum":"ETH",
    "Solana":"SOL",
    "Ripples":"XRP",
    "Cardano":"ADA",
    "Binancecoin":"BNB"
}

df_ajustado = df_requisicao.stack(0).unstack(0)
df_ajustado["data_coleta"] = datetime.datetime.now()
df_ajustado = df_ajustado.reset_index(drop=False)
df_ajustado.rename(columns={"index":"coin"}, inplace=True)
df_ajustado["coin"] = df_ajustado["coin"].str.title()
df_ajustado["ticker"] = df_ajustado["coin"].map(tickers)

df_ajustado.dtypes

# CONEXÃO E CARGA SQLITE

conexao = sqlite3.connect("data/crypto_analytics.db")
df_ajustado.to_sql(name="tb_crypto_api", con=conexao, if_exists="append", index=False)
conexao.close()
