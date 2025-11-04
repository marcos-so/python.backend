cache_users = {}

def obter_usuario(user_id: int):
    if user_id in cache_users:
        print(f"Cache HIT para user {user_id}")
        return cache_users[user_id]

    print(f"Cache MISS para user {user_id}")
    # Simulando uma busca no banco de dados
    usuario = {
        "id": user_id,
        "nome": f"Usuário{user_id}",
        "email": f"usuario{user_id}@example.com",
        "ativo": True
    }
    cache_users[user_id] = usuario
    return usuario

user1 = obter_usuario(123) #Cache MISS
user2 = obter_usuario(123) #Cache HIT
user3 = obter_usuario(456) #Cache MISS

print(f"\nTotal em cache: {len(cache_users)}")
print(f"IDs em cache: {list(cache_users.keys())}")