import random
from datetime import datetime, timedelta

METODOS = ["GET", "POST", "PUT", "DELETE", "PATCH"]
ENDPOINTS = [
    "/api/products/123", "/api/products/456", "/api/products/789",
    "/api/orders", "/api/orders/999", "/api/users/789", "/api/users/123",
    "/api/cart", "/api/checkout"
]
STATUS = [200, 201, 204, 400, 401, 404, 500, 502, 503]
USER_IDS = [f"user_{i}" for i in range(1, 151)]
NOME_ARQUIVO = "api_logs.txt"
TOTAL_LINHAS = 100000

def gerar_logs():
    timestamp_inicial = datetime(2024, 10, 11, 10, 0, 0)

    with open(NOME_ARQUIVO, "w") as f:
        for i in range(TOTAL_LINHAS):
            timestamp = timestamp_inicial + timedelta(seconds=i)
            metodo = random.choices(METODOS, weights=[0.6, 0.2, 0.1, 0.05, 0.05], k=1)[0]
            endpoint = random.choice(ENDPOINTS)
            status = random.choices(STATUS, weights=[0.7, 0.1, 0.05, 0.05, 0.03, 0.03, 0.02, 0.01, 0.01], k=1)[0]
            tempo_resposta = f"{random.randint(20, 1500)}ms"
            user_id = random.choice(USER_IDS)

            linha_log = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')}|{metodo}|{endpoint}|{status}|{tempo_resposta}|{user_id}\n"
            f.write(linha_log)

    print(f"Arquivo '{NOME_ARQUIVO}' gerado com {TOTAL_LINHAS} linhas.")

if __name__ == "__main__":
    gerar_logs()