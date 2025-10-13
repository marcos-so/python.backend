tempos_resposta = [50, 120, 450, 1200, 80, 950]
for tempo in tempos_resposta:
    if tempo <= 50:
        print(f"Tempo de resposta {tempo}ms: Excelente")
    elif tempo <= 120:
        print(f"Tempo de resposta {tempo}ms: Bom")
    elif tempo <= 500:
        print(f"Tempo de resposta {tempo}ms: Médio")
    else:
        print(f"Tempo de resposta {tempo}ms: Lento")