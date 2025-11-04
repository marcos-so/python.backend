def ler_logs_do_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r") as f:
            for linha in f:
                yield linha.strip()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return

def formatar_e_imprimir_relatorio(metricas):
    print("--- Relatório de Uso da API ---")
    print(f"Total de Requisições: {metricas.get('total_requisicoes', 0)}")
    print(f"Total de Erros (status >= 400): {metricas.get('total_erros', 0)}")

    print("\nRequisições por Método HTTP:")
    for metodo, total in metricas.get('por_metodo', {}).items():
        print(f"  - {metodo}: {total}")

    print(f"\nEndpoint Mais Acessado: {metricas.get('endpoint_mais_acessado', 'N/A')}")
    print(f"Usuário com Mais Requisições: {metricas.get('usuario_mais_ativo', 'N/A')}")
    print("---------------------------------")