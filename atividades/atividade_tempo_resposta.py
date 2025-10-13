tempos_resposta = [50, 120, 450, 1200, 80, 950]
for tempo in tempos_resposta:
    if tempo <= 50:
        print(f"{tempo}ms: Excelente")
    elif tempo <= 120:
        print(f"{tempo}ms: Bom")
    elif tempo <= 450:
        print(f"{tempo}ms: Médio")
    else:
        print(f"{tempo}ms: Lento")