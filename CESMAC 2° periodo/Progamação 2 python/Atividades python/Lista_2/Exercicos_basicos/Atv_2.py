n = int(input("Digite o limite: "))
num = 0
while num <= 100:
    print(num)
    num += 1
    if num == n:
        print(f"Chegou ao número {n}, parando a contagem.")
        break