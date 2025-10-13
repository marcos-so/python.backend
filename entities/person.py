class Person:
    def __init__(self, name: str, age: int, cpf: str):
        self.name = name
        self.age = age
        self._cpf = cpf

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, value: str):
        if len(value) != 11 or not value.isdigit():
            raise ValueError("CPF must be an 11-digit number.")
        self._cpf = value

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def __str__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self) -> str:
        return f"Pessoa(name={self.name!r}, age={self.age!r})"

    # Exemplo de uso
if __name__ == "__main__":
    person = Person("Marcos", 30, "12345678901")
    print(person)
    print(person.cpf)