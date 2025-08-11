def validar_dados():
    
    while True:
        nome = input("Digite seu nome: ")
        if len(nome) > 3:
            break
        print("Nome deve ter mais de 3 caracteres.")

    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if 0 <= idade <= 150:
                break
            print("Idade deve estar entre 0 e 150.")
        except ValueError:
            print("Digite um número válido.")

    while True:
        try:
            salario = float(input("Digite seu salário: "))
            if salario > 0:
                break
            print("Salário deve ser maior que zero.")
        except ValueError:
            print("Digite um valor válido.")

    while True:
        sexo = input("Digite seu sexo (f/m): ").lower()
        if sexo in ['f', 'm']:
            break
        print("Sexo deve ser 'f' ou 'm'.")

    while True:
        estado_civil = input("Digite seu estado civil (s/c/v/d): ").lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            break
        print("Estado civil deve ser 's', 'c', 'v' ou 'd'.")

    print("\n--- Dados Validados ---")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: R${salario:.2f}")
    print(f"Sexo: {sexo}")
    print(f"Estado Civil: {estado_civil}")

validar_dados()
