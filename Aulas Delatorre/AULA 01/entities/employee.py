class Employee:
    def __init__(self, nome: str, cargo: str, salario: float):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def calcular_bonus(self) -> float:
        return self.salario * 0.1
