n = int(input("Quantos números? "))

numeros = []
for i in range(n):
    num = float(input(f"Número {i+1}: "))
    numeros.append(num)

print(f"Menor: {min(numeros)}")
print(f"Maior: {max(numeros)}")
print(f"Soma: {sum(numeros)}")
