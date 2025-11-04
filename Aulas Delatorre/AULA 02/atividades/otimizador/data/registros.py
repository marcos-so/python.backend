import random
import string

def gerar_registros(qtd=1_000_000):
    registros = []
    for i in range(1, qtd + 1):
        nome = f"Usuario{i}"
        email = f"usuario{i}@exemplo.com"
        registros.append({
            "id": i,
            "nome": nome,
            "email": email
        })
    return registros

if __name__ == "__main__":
    users = gerar_registros(10)
    print(users[:3])