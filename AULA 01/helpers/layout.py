def separadores():
    print("=" * 43)

def exibir_menu():
    separadores()
    print("|  Menu de Gerenciamento de Funcionários  |")
    separadores()
    print("    1 - Cadastrar novo funcionário")
    print("    2 - Listar funcionários")
    print("    3 - Listar funcionários por cargo")
    print("    4 - Calcular folha de pagamento total")
    print("    5 - Encerrar aplicação")
    return input("\nDigite a opção desejada: ")