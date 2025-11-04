numeros = [1,2,3,4,5]
quadrados = [x**2 for x in numeros]

print(quadrados)

pares = [x for x in numeros if x % 2 == 0]
print(pares)