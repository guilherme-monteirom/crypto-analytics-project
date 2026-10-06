import psycopg2
import os
from dotenv import load_dotenv
import datetime
import requests
from psycopg2.extras import Json

load_dotenv()
user = os.getenv("user")
password = os.getenv("password")
port = os.getenv("port")
coingecko_apikey = os.getenv("coingecko_apikey")

try:
    conexao = psycopg2.connect(
        host = "localhost",
        database = "crypto_analytics",
        user = user,
        password = password,
        port = port
    )
    print("Conectado com sucesso!")
except Exception as e:
    print(repr(e))

requisicao = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,ripples,cardano,binancecoin&vs_currencies=usd,eur,brl&include_market_cap=true&include_24hr_change=true/x-cg-demo-api-key:{coingecko_apikey}")

dado = requisicao.json()

cursor = conexao.cursor()

cursor.execute(
    """
    INSERT INTO crypto_raw (data_coleta, payload)
    VALUES (NOW(), %s);
    """,
    (Json(dado),)
)

conexao.commit()

print("Registro realizado!")

cursor.close()
conexao.close()