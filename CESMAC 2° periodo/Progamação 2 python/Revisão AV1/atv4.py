def celsius():
    print("Voce selecinou: 'Converter Celsius para Farenheint'\n")
    temp = float(input("Digite a temperatura"))
    conversão = (9/5*temp+32)
    print(f"{conversão:.2f}°F")
def faren():
    print("Voce selecinou: 'Converter Farenheint para Celsius'\n")
    temp = float(input("Digite a temperatura "))
    conversão = (temp-32)*(5/9)
    print(f"{conversão:.2f}°C")
def para():
    print("Saiu")
    
print("Conversão de escalas")
print("1-Converter Celsius para Farenheint\n 2-Converter Farenheint para Celsius\n 3-Sair")
select = int(input("Digite "))

match select:
    case 1: celsius()
    case 2: faren()
    case 3: para()
    case _: print("invalido")
    