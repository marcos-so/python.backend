def create_user(name: str, age: int) -> dict[str, object]:
    return {"name": name, "age": age}

user_id = 1
user_name = "Marcos"
user_email = "marcos.souza@example.com"
active_account = True
user_tags = ["admin", "backend", "api", "user"]

profile = create_user(user_name, 30)

print(profile)
