produtos = [
    {'nome': 'Produto 1', 'preco': 50},
    {'nome': 'Produto 2', 'preco': 60},
    {'nome': 'Produto 3', 'preco': 75},
    {'nome': 'Produto 4', 'preco': 100}
]


for produto in produtos:
    print(f"{produto['nome']} - {produto['preco']} R$")