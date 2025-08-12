import pandas as pd
import requests
import json
import config

# Le a planilha Seguradora
df_planilha = pd.read_excel("DB_Seguradora.xlsx")

# Converte de lista para dicionario
dados = df_planilha.to_dict(orient="records")

# Insere cabeçalhos
headers = {
    "Content-Type": "application/json",
    "api-key": config.MONGO_API_KEY
}

# Requisiçao
payload = {
    "dataSource": config.MONGO_CLUSTER,
    "database": config.MONGO_DATABASE,
    "collection": config.MONGO_COLLECTION,
    "documents": dados
}

# Metodo POST
response = requests.post(
    config.MONGO_DATA_API_URL,
    headers=headers,
    data=json.dumps(payload)
)

# Resposta (Post)
print("Status:", response.status_code)
print("Resposta:", response.json())
