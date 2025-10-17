def buscar_usuario(criterio, valor, indices):
    indice_id, indice_email, indice_nome = indices

    if criterio == "id":
        return indice_id.get(valor)
    elif criterio == "email":
        return indice_email.get(valor)
    elif criterio == "nome":
        return indice_nome.get(valor)
    else:
        raise ValueError("Critério inválido. Use: id, email ou nome.")