print("Responda 'Sim' ou 'Não' para as perguntas a seguir.\n")
pergunta_1 = input("Telefobou para a vitima? ").strip().lower()
pergunta_2 = input("Esteve no local do crime? ").strip().lower()
pergunta_3 = input("Mora perto da vitima? ").strip().lower()
pergunta_4 = input("Devia para a vitima? ").strip().lower()
pergunta_5 = input("Já trabalhou com a vitima? ").strip().lower()
respostas = [pergunta_1, pergunta_2, pergunta_3, pergunta_4, pergunta_5]
if respostas.count('sim') == 2:
    print("Suspeita")
elif respostas.count('sim') in [3, 4]:
    print("Cúmplice")
elif respostas.count('sim') == 5:
    print("Assassino")
else:
    print("Inocente")
