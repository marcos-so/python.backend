class Employee:
    def __init__(self, nome: str, cargo: str, salario: float):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def calcular_bonus(self) -> float:
        return self.salario * 0.1

# gerenciador.py
def adicionar_funcionario(lista: list, funcionario):
    lista.append(funcionario)

def listar_funcionarios(lista: list) -> list:
    return lista

def atualizar_funcionario(lista: list, nome: str, novo_cargo: str, novo_salario: float) -> bool:
    for funcionario in lista:
        if funcionario.nome == nome:
            funcionario.cargo = novo_cargo
            funcionario.salario = novo_salario
            return True
    return False

def remover_funcionario(lista: list, nome: str) -> bool:
    for i, funcionario in enumerate(lista):
        if funcionario.nome == nome:
            del lista[i]
            return True
    return False

def listar_por_cargo(lista: list, cargo: str) -> list:
    return [funcionario for funcionario in lista if funcionario.cargo == cargo]

def calcular_folha_total(lista: list) -> float:
    return sum(funcionario.salario + funcionario.calcular_bonus() for funcionario in lista)