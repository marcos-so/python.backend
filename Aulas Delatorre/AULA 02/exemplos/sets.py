tecnologias = {"Python", "Java", "JavaScript", "Python"}
print(tecnologias)


# Operações de conjuntos
backend_devs = {"Ana", "Bruno", "Carlos"}
frontend_devs = {"Bruno", "Diana", "Elena"}

# Interseção (quem faz ambos?)
fullstack = backend_devs & frontend_devs  # {'Bruno'}

# União (todos os devs)
todos_devs = backend_devs | frontend_devs

# Diferença (só backend)
so_backend = backend_devs - frontend_devs  # {'Ana', 'Carlos'}