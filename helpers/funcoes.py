import entities.employee as emp

def buscar_funcionarios():
    employees = []
    for employee in emp.listar_funcionarios(employees):
        employees.append(employee)
        print(f"Nome: {employee.nome}, Cargo: {employee.cargo}, Salário: {employee.salario}")

    return employees

def adicionar_funcionario(name: str, position: str, salary: float):
    print(f"Adicionando funcionário: {name}, Cargo: {position}, Salário: {salary}")

    new_employee = emp.Employee(name, position, salary)
    return new_employee