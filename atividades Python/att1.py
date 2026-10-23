produtos = {
    101: {"nome": "Teclado", "preco": 120.00, "estoque": 10},
    102: {"nome": "Mouse", "preco": 65.00, "estoque": 15},
    103: {"nome": "Monitor", "preco": 850.00, "estoque": 5},
    104: {"nome": "Webcam", "preco": 180.00, "estoque": 8},
    105: {"nome": "Headset", "preco": 145.00, "estoque": 12},
    106: {"nome": "Pendrive 64GB", "preco": 45.00, "estoque": 30},
    107: {"nome": "SSD 480GB", "preco": 280.00, "estoque": 7},
    108: {"nome": "HD Externo 1TB", "preco": 350.00, "estoque": 6},
    109: {"nome": "Memória RAM 8GB", "preco": 160.00, "estoque": 14},
    110: {"nome": "Placa de Vídeo", "preco": 1850.00, "estoque": 3},
    111: {"nome": "Processador", "preco": 950.00, "estoque": 4},
    112: {"nome": "Placa-mãe", "preco": 680.00, "estoque": 5},
    113: {"nome": "Fonte 600W", "preco": 320.00, "estoque": 9},
    114: {"nome": "Gabinete", "preco": 250.00, "estoque": 6},
    115: {"nome": "Caixa de Som", "preco": 95.00, "estoque": 11}
}

print(produtos[102]["nome"], produtos[102]["preco"])

produtos[101]["preco"] = 135.00

produtos[104] = {"nome": "Webcam", "preco": 180.00, "estoque": 8}
del produtos[103]

for codigo, dados in produtos.items():
    print(f"Código: {codigo} | Nome: {dados['nome']} | Preço: R$ {dados['preco']:.2f} | Estoque: {dados['estoque']}")

total = 0

for codigo, dados in produtos.items():
    total += dados["preco"] * dados["estoque"]
print(f"Valor total do estoque: R$ {total:.2f}")