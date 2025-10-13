def main():
    user_id = 1
    user_name = "Marcos"
    user_email = "marcos.souza@example.com"
    active_account = True
    user_tags = ["admin", "backend", "api", "user"]

    profile = create_user(user_name, 30)

    def create_user(name: str, age: int) -> dict[str, int]:
        return {"name": name, "age": age}



if __name__ == "__main__":
    main()
