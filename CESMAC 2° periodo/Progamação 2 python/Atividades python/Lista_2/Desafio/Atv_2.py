
N = int(input("Digite a quantidade de números: "))

numeros = []

for i in range(N):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

print("\n--- Resultados ---")
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")
