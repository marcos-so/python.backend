# List comprehension - Colchetes []
lista = [x for x in range(5)]
print(type(lista))  # <class 'list'>
print(lista)        # [0, 1, 2, 3, 4]

# Generator expression - Parênteses ()
gerador = (x for x in range(5))
print(type(gerador))  # <class 'generator'>
print(gerador)        # <generator object> - não mostra valores!

# Para consumir:
for valor in gerador:
  print(valor)  # Imprime 1 de cada vez


def fibonacci(n):
  a, b = 0, 1
  for _ in range(n):
    yield a  # yield transforma a função em um gerador
    a, b = b, a + b