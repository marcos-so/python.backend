# Dicionário por compreensão
quadrados = {x: x**2 for x in range(5)}

# Mesclando dicionários (Python 3.9+)
config_default = {"timeout": 30, "retries": 3}
config_user = {"timeout": 60, "retries": 5}

config_final = config_default | config_user
print(config_final)

api_response = {
    "status": "success",
    "data": {
        "usuarios": [
            {"id": 1, "nome": "Ana"},
            {"id": 2, "nome": "Bruno"},
            {"id": 3, "nome": "Carlos"},
        ],
        "meta": {"total": 3, "page": 1}
    }
}

primeiro_usuario = api_response.get("data", {}).get("usuarios", [])[0]
print(primeiro_usuario)
