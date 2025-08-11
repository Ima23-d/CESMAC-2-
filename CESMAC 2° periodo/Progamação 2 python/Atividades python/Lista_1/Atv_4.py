nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

while nota_1 < 0 or nota_1 > 10 or nota_2 < 0 or nota_2 > 10:
    print("Notas devem estar entre 0 e 10. Tente novamente.")
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))
media = (nota_1 + nota_2) / 2
if media == 10:
    print(f"Media: {media} Aprovado com distinção")
elif media >= 7:
    print(f"Media: {media} Aprovado")
else:
    print(f"Media: {media} Reprovado")