logs = [
    ("2025-10-20 10:00:00", "GET", "/api/users", 200),
    ("2025-10-20 10:05:00", "POST", "/api/orders", 201),
    ("2025-10-20 10:10:00", "GET", "/api/users", 500),
    ("2025-10-20 10:15:00", "DELETE", "/api/orders/123", 204),
]

erros = [log for log in logs if log[3] >= 400]

metodos = [log[1] for log in logs]

print(f"GET: {metodos.count('GET')}")
print(f"POST: {metodos.count('POST')}")
print(f"DELETE: {metodos.count('DELETE')}")

ultimos_logs = logs[-2:]
print(f"Últimos logs:{ultimos_logs}")

logs_ordenados = sorted(logs, key=lambda log: log[3], reverse=True)
print(logs_ordenados)

print(f"Logs com erros: {len(erros)}")