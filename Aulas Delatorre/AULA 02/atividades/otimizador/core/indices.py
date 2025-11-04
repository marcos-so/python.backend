def criar_indices(registros):
    indice_id = {}
    indice_email = {}
    indice_nome = {}

    for user in registros:
        indice_id[user["id"]] = user
        indice_email[user["email"]] = user
        indice_nome[user["nome"]] = user

    return indice_id, indice_email, indice_nome