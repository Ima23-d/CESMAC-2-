print("Qual turno você estuda?\n")
print("M - Matutino")
print("V - Vespertino")
print("N - Noturno")
turno = input("Digite a letra correspondente ao seu turno: ").upper()
match turno:
    case 'M':
        print("Bom dia!")
    case 'V':
        print("Boa tarde!")
    case 'N':
        print("Boa noite!")
    case _:
        print("Turno inválido!")