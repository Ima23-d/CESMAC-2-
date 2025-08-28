nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >=7:
    print(f"Media: {media:.2f} Aprovado")
elif media <7 and media >=4:
    print(f"Media: {media:.2f} Reposição")
else:
    print(f"Media: {media:.2f} Reprovado")