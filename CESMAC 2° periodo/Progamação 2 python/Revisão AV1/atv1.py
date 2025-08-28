valor  = int(input("Digite um valor inteiro"))
while (valor <=0):
    print("Valor invalido!\n")
    valor  = int(input("Digite um valor inteiro"))
    
print(f"Numeros pares até: {valor}")
for i in range(2,valor+1,2):
    print(i, end=",")

print(f"\nNumeros impares até {valor}")
for i in range(1, valor + 1,2):
    print(i,end=",")