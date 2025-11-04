from collections import Counter

def analisar_logs(gerador_de_linhas):

    def extrair_dados(linhas):
        for linha in linhas:
            try:
                _timestamp, metodo, endpoint, status_str, _tempo, user_id = linha.split('|')
                yield (metodo, endpoint, int(status_str), user_id)
            except (ValueError, IndexError):
                continue

    contagem_metodos = Counter()
    contagem_endpoints = Counter()
    contagem_usuarios = Counter()
    total_erros = 0
    total_requisicoes = 0

    for metodo, endpoint, status, user_id in extrair_dados(gerador_de_linhas):
        total_requisicoes += 1
        contagem_metodos[metodo] += 1
        contagem_endpoints[endpoint] += 1
        contagem_usuarios[user_id] += 1

        if status >= 400:
            total_erros += 1

    endpoint_mais_acessado = contagem_endpoints.most_common(1)[0][0] if contagem_endpoints else None
    usuario_mais_ativo = contagem_usuarios.most_common(1)[0][0] if contagem_usuarios else None

    metricas = {
        "total_requisicoes": total_requisicoes,
        "por_metodo": dict(contagem_metodos),
        "total_erros": total_erros,
        "endpoint_mais_acessado": endpoint_mais_acessado,
        "usuario_mais_ativo": usuario_mais_ativo,
    }

    return metricas