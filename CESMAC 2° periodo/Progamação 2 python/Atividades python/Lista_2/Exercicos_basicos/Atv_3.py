print("Operação adição!\n")
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
while True:
    print(f"A soma de '{n1}' e '{n2}' é: '{n1 + n2}'")
    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        print("Operação encerrada.")
        break
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))