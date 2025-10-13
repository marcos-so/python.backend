# Argumentos especiais que passamos para as funções
# exemplo de args
# def soma(*args):
#     total = 0
#     for numero in args:
#         total += numero
#     return total

# resultado = soma(1, 2, 3, 4, 5)
# print(f"Soma: {resultado}")

# exemplo de kwargs
# def exibir_usuario(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f"{chave}: {valor}")

# exibir_usuario(nome="Marcos", idade=30, email="marcos.souza@example.com")

def funcao_completa(obrigatorio, opcional=2, *args,  **kwargs):
    print(f"Obrigatório: {obrigatorio}")
    print(f"Opcional: {opcional}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

funcao_completa(1, 3, 4, 5, 6, nome="Marcos", idade=30)