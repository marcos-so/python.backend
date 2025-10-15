# Você tem uma lista de pedidos. Cada pedido é uma tupla: (id, cliente, valor, status).
# Extraia: (1) Pedidos pendentes, (2) Valor total, (3) Cliente com mais pedidos.

pedidos = [
    (1, "Ana", 150.00, "pago"),
    (2, "Bruno", 200.00, "pendente"),
    (3, "Ana", 100.00, "pago"),
    (4, "Carlos", 300.00, "pendente"),
    (5, "Ana", 50.00, "cancelado"),
]

pendentes = [pedido for pedido in pedidos if pedido[3] == 'pendente']
valor_total = sum(pedido[2] for pedido in pedidos)
clientes_mais_pedidos = max(set(pedido[1] for pedido in pedidos), key=lambda cliente: sum(1 for pedido in pedidos if pedido[1] == cliente))

print(f"Pedidos pendentes: {pendentes}")
print(f"Valor total dos pedidos: R$ {valor_total:.2f}")
print(f"Cliente com mais pedidos: {clientes_mais_pedidos}")