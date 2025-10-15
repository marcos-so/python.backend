pedidos = [
    {"cliente": "Ana", "valor": 50.00},
    {"cliente": "Bruno", "valor": 150.00},
    {"cliente": "Ana", "valor": 80.00},   # Ana: 130 total
    {"cliente": "Carlos", "valor": 30.00},
    {"cliente": "Bruno", "valor": 50.00}, # Bruno: 200 total
]

clientes = {p["cliente"] for p in pedidos}

totais = {
    cliente: sum(p["valor"] for p in pedidos if p["cliente"] == cliente)
    for cliente in clientes
    if sum(p["valor"] for p in pedidos if p["cliente"] == cliente) > 100
}

print(totais)

# resolução do professor

from collections import defaultdict
totais = defaultdict(float)

for p in pedidos:
    totais[p["cliente"]] += p["valor"]

cliente_vip = {cliente: total for cliente, total in totais.items() if total > 100}

print(cliente_vip)
