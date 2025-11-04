# atividades/atividade_tempo_resposta.py
def atividade_tempo_resposta():
    tempos_resposta = [50, 120, 450, 1200, 80, 950]
    for tempo in tempos_resposta:
        classificacao = ""
        if tempo <= 50:
            classificacao = "Excelente"
        elif tempo <= 120:
            classificacao = "Bom"
        elif tempo <= 450:
            classificacao = "Médio"
        else:
            classificacao = "Lento"

        print(f"{tempo}ms: {classificacao}")