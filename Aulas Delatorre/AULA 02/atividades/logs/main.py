import pathlib
from processador import analisar_logs
from utils import ler_logs_do_arquivo, formatar_e_imprimir_relatorio

def main():
    diretorio_do_script = pathlib.Path(__file__).parent.resolve()

    caminho_arquivo_log = diretorio_do_script / "api_logs.txt"

    gerador_de_linhas_log = ler_logs_do_arquivo(caminho_arquivo_log)

    if not gerador_de_linhas_log:
        return

    metricas_resultado = analisar_logs(gerador_de_linhas_log)

    formatar_e_imprimir_relatorio(metricas_resultado)

if __name__ == "__main__":
    main()