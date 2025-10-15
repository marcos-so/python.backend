from entities.employee import Employee

def adicionar_funcionario(lista: list, nome: str, cargo: str, salario: float) -> bool:
    if not nome.strip() or salario <= 0:
        return False
    novo = Employee(nome, cargo, salario)
    lista.append(novo)
    return True

def buscar_funcionarios(lista: list):
    if not lista:
        print("Nenhum funcionário cadastrado.\n")
        return
    for f in lista:
        print(f"Nome: {f.nome}, Cargo: {f.cargo}, Salário: {f.salario}, Bônus: {f.calcular_bonus():.2f}")
    print()

def listar_por_cargo(lista: list, cargo: str) -> list:
    return [f for f in lista if f.cargo.lower() == cargo.lower()]

def calcular_folha_total(lista: list) -> float:
    return sum(f.salario + f.calcular_bonus() for f in lista)
