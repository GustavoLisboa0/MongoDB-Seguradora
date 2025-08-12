import pandas as pd
import requests
import json
import config

# 1. Ler a planilha Excel
df_planilha = pd.read_excel("DB_Seguradora.xlsx")

# 2. Converter para lista de dicionários
dados = df_planilha.to_dict(orient="records")

# 3. Cabeçalhos da requisição
headers = {
    "Content-Type": "application/json",
    "api-key": config.MONGO_API_KEY
}

# 4. Corpo da requisição
payload = {
    "dataSource": config.MONGO_CLUSTER,
    "database": config.MONGO_DATABASE,
    "collection": config.MONGO_COLLECTION,
    "documents": dados
}

# 5. Enviar via POST
response = requests.post(
    config.MONGO_DATA_API_URL,
    headers=headers,
    data=json.dumps(payload)
)

# 6. Exibir resposta
print("Status:", response.status_code)
print("Resposta:", response.json())
