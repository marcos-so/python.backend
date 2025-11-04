while True:
    numero = input("Digite um número ou 'q' para sair: ")
    if numero.isdigit():
        numero = int(numero)
        if numero % 3 == 0 and numero % 5 == 0:
            print("FizzBuzz")
        elif numero % 3 == 0:
            print("Fizz")
        elif numero % 5 == 0:
            print("Buzz")
        else:
            print(f'O número {numero} não é divisível por 3 e nem por 5')
    else:
        if numero == 'q':
            break
        print("Entrada inválida. Por favor, digite um número inteiro ou 'q' para encerrar a aplicação.")