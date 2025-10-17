import time

def busca_linear(criterio, valor, registros):
    for user in registros:
        if user[criterio] == valor:
            return user
    return None


def benchmark_buscas(registros, indices, criterio, valor):
    inicio = time.perf_counter()
    from core.busca import buscar_usuario
    resultado_indexado = buscar_usuario(criterio, valor, indices)
    tempo_indexado = time.perf_counter() - inicio

    inicio = time.perf_counter()
    resultado_linear = busca_linear(criterio, valor, registros)
    tempo_linear = time.perf_counter() - inicio

    return {
        "criterio": criterio,
        "valor": valor,
        "resultado_indexado": resultado_indexado,
        "resultado_linear": resultado_linear,
        "tempo_indexado": tempo_indexado,
        "tempo_linear": tempo_linear,
        "aceleracao": tempo_linear / tempo_indexado if tempo_indexado > 0 else float('inf')
    }