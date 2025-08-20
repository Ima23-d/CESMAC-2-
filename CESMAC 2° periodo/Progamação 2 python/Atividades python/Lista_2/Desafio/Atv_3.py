while True:
    n = int(input("Quantos números (entre 1 e 1000)? "))
    if 1 <= n <= 1000:
        break
    else:
        print("Erro! Digite uma quantidade entre 1 e 1000.")

numeros = []
for i in range(n):
    while True:
        num = float(input(f"Número {i+1}: "))
        if 0 <= num <= 1000:
            numeros.append(num)
            break
        else:
            print("Erro! Digite um número entre 0 e 1000.")

print(f"Menor: {min(numeros)}")
print(f"Maior: {max(numeros)}")
print(f"Soma: {sum(numeros)}")

