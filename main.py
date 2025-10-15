import helpers.layout as layout
import helpers.funcoes as funcoes

def main():
    funcionarios = []

    while True:
        opcao = layout.exibir_menu()

        if opcao == "1":
            nome = input("Nome: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))
            if funcoes.adicionar_funcionario(funcionarios, nome, cargo, salario):
                print("Funcionário adicionado com sucesso.\n")
            else:
                print("Erro ao adicionar funcionário. Verifique os dados.\n")

        elif opcao == "2":
            layout.separadores()
            print("Listar funcionários")
            funcoes.buscar_funcionarios(funcionarios)

        elif opcao == "3":
            cargo = input("Digite o cargo: ")
            layout.separadores()
            print(f"Funcionários com cargo: {cargo}")
            lista = funcoes.listar_por_cargo(funcionarios, cargo)
            if lista:
                for func in lista:
                    print(f"Nome: {func.nome}, Cargo: {func.cargo}, Salário: {func.salario}")
            else:
                print("Nenhum funcionário encontrado.")
            print()

        elif opcao == "4":
            total = funcoes.calcular_folha_total(funcionarios)
            print(f"Folha de pagamento total (com bônus): R$ {total:.2f}\n")

        elif opcao == "5":
            print("Encerrando aplicação.")
            break

        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
