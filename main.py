import entities.employee as emp
import helpers.layout as layout
import helpers.funcoes as funcoes

def main():
    employee = []

    while (True):
        opcao = layout.exibir_menu()

        if opcao == "1":
            name = input("Nome: ")
            position = input("Cargo: ")
            salary = float(input("Salário: "))
            funcoes.adicionar_funcionario(name, position, salary)
            print("Funcionário adicionado com sucesso.")
            continue
        elif opcao == "2":
            layout.separadores()
            print("Listar funcionários")
            employees = funcoes.buscar_funcionarios()
            print(f"Total de funcionários: {len(employees)}")
            print(employees)
            continue
        elif opcao == "3":
            cargo = input("Digite o cargo: ")
            print(f"Listar funcionários do cargo: {cargo}")
            for func in emp.listar_por_cargo(employee, cargo):
                print(f"Nome: {func.nome}, Cargo: {func.cargo}, Salário: {func.salario}")
            continue
        elif opcao == "4":
            name = input("Nome do funcionário a ser atualizado: ")
            new_position = input("Novo cargo: ")
            new_salary = float(input("Novo salário: "))
            if emp.atualizar_funcionario(employee, name, new_position, new_salary):
                print("Funcionário atualizado com sucesso.")
            else:
                print("Funcionário não encontrado.")
            continue
        elif opcao == "5":
            name = input("Nome do funcionário a ser removido: ")
            if emp.remover_funcionario(employee, name):
                print("Funcionário removido com sucesso.")
            else:
                print("Funcionário não encontrado.")
            continue
        elif opcao == "6":
            print("Encerrando aplicação.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue



if __name__ == "__main__":
    main()
