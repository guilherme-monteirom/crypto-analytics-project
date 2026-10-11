import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

user = os.getenv("user")
password = os.getenv("password")
port = os.getenv("port")
host = "localhost"
database= "crypto_analytics"

try:
    conexao = psycopg2.connect(
        host = host,
        database = database,
        user = user,
        password = password,
        port = port
    )
    print("Conectado com sucesso!")
except Exception as e:
    print(repr(e))

query_max_id = """
SELECT COALESCE(MAX(id_raw),0)
FROM crypto_silver
"""

with conexao.cursor() as cursor:
    
    cursor.execute(query_max_id)

    ultimo_id_processado = cursor.fetchone()[0]

print(ultimo_id_processado)

query = f"""SELECT * FROM crypto_raw
    WHERE id > {ultimo_id_processado};"""

with conexao.cursor() as cursor:
    cursor.execute(query)

    dados_raw = cursor.fetchall()

    colunas = [desc[0] for desc in cursor.description]

conexao.close()

df_raw = pd.DataFrame(dados_raw, columns=colunas)

registros = []

for _, linha in df_raw.iterrows():

    id_raw = linha["id"]

    payload = linha["payload"]
    data_coleta = linha["data_coleta"]

    for coin, info in payload.items():
        registros.append({
            "id_raw": id_raw,
            "coin": coin,
            "usd": info["usd"],
            "usd_market_cap": info["usd_market_cap"],
            "eur": info["eur"],
            "eur_market_cap": info["eur_market_cap"],
            "brl": info["brl"],
            "brl_market_cap": info["brl_market_cap"],
            "data_coleta": data_coleta
        })

df_silver = pd.DataFrame(registros)

tickers = {
    "Bitcoin":"BTC",
    "Ethereum":"ETH",
    "Solana":"SOL",
    "Ripples":"XRP",
    "Cardano":"ADA",
    "Binancecoin":"BNB"
}

df_silver["coin"] = df_silver["coin"].str.title()
df_silver["tickers"] = df_silver["coin"].map(tickers)
df_silver.rename(columns={"index":"id_raw"})

conexao = psycopg2.connect(
    host= host,
    database=  database,
    user= user,
    password= password,
    port= port
)

query_insert = """
INSERT INTO crypto_silver (
    id_raw,
    coin,
    ticker,
    usd,
    usd_market_cap,
    eur,
    eur_market_cap,
    brl,
    brl_market_cap,
    data_coleta)
VALUES (
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s
)"""

with conexao.cursor() as cursor:

    for _, linha in df_silver.iterrows():

        cursor.execute(
            query_insert,
            (
                linha["id_raw"],
                linha["coin"],
                linha["tickers"],
                linha["usd"],
                linha["usd_market_cap"],
                linha["eur"],
                linha["eur_market_cap"],
                linha["brl"],
                linha["brl_market_cap"],
                linha["data_coleta"]
            )
        )
    conexao.commit()
conexao.close()

print("Carga concluída")