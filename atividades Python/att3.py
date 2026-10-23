cardapio = {
    1: {"nome": "Hambúrguer", "preco": 25.00},
    2: {"nome": "Batata frita", "preco": 12.00},
    3: {"nome": "Suco", "preco": 8.00},
    4: {"nome": "Refrigerante", "preco": 7.00},
    5: {"nome": "Cheeseburger", "preco": 28.00},
    6: {"nome": "X-Bacon", "preco": 32.00},
    7: {"nome": "X-Salada", "preco": 27.00},
    8: {"nome": "Pizza individual", "preco": 30.00},
    9: {"nome": "Cachorro-quente", "preco": 18.00},
    10: {"nome": "Pastel", "preco": 10.00},
    11: {"nome": "Água mineral", "preco": 4.00},
    12: {"nome": "Milk-shake", "preco": 16.00},
    13: {"nome": "Sorvete", "preco": 9.00},
    14: {"nome": "Café", "preco": 5.00},
    15: {"nome": "Brownie", "preco": 11.00}
}

pedidos = {
    1: {1: 2, 2: 3, 3: 2},
    2: {5: 2, 4: 2, 13: 1},
    3: {6: 1, 2: 2, 11: 2},
    4: {8: 2, 3: 3},
    5: {9: 3, 10: 2, 4: 3},
    6: {7: 2, 12: 2, 14: 2},
    7: {1: 1, 5: 1, 2: 2},
    8: {10: 4, 11: 3},
    9: {6: 2, 3: 2, 15: 2},
    10: {8: 1, 13: 3, 14: 2},
    11: {9: 2, 4: 2, 12: 1},
    12: {5: 3, 2: 3, 3: 3},
    13: {7: 1, 1: 2, 15: 1},
    14: {6: 1, 8: 1, 11: 4},
    15: {12: 3, 13: 2, 10: 2}
}

opcao = 0

while opcao != 8:
    print("\n===== LANCHONETE =====")
    print("1 - Consultar cardápio")
    print("2 - Consultar pedido da mesa")
    print("3 - Realizar pedido")
    print("4 - Alterar quantidade de um item")
    print("5 - Remover item do pedido")
    print("6 - Calcular a conta da mesa")
    print("7 - Listar mesas com pedidos")
    print("8 - Encerrar o programa")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        for codigo, produto in cardapio.items():
            print(f"{codigo} - {produto['nome']} - R$ {produto['preco']:.2f}")

    elif opcao == 2:
        mesa = int(input("Número da mesa: "))
        if mesa in pedidos:
            for codigo, qtd in pedidos[mesa].items():
                print(f"{cardapio[codigo]['nome']} | Quantidade: {qtd} | Preço unitário: R$ {cardapio[codigo]['preco']:.2f}")
        else:
            print("Essa mesa não possui pedidos.")

    elif opcao == 3:
        mesa = int(input("Número da mesa: "))
        codigo = int(input("Código do produto: "))
        qtd = int(input("Quantidade: "))
        if codigo not in cardapio:
            print("Produto não existe no cardápio.")
        elif qtd <= 0:
            print("Quantidade inválida.")
        else:
            if mesa not in pedidos:
                pedidos[mesa] = {}
            if codigo in pedidos[mesa]:
                pedidos[mesa][codigo] += qtd
            else:
                pedidos[mesa][codigo] = qtd
            print("Pedido registrado.")

    elif opcao == 4:
        mesa = int(input("Número da mesa: "))
        codigo = int(input("Código do produto: "))
        if mesa in pedidos and codigo in pedidos[mesa]:
            nova_qtd = int(input("Nova quantidade: "))
            if nova_qtd > 0:
                pedidos[mesa][codigo] = nova_qtd
                print("Quantidade alterada.")
            else:
                print("Quantidade inválida. Para tirar o item, use a opção 5.")
        else:
            print("Mesa ou produto não encontrado no pedido.")

    elif opcao == 5:
        mesa = int(input("Número da mesa: "))
        codigo = int(input("Código do produto: "))
        if mesa in pedidos and codigo in pedidos[mesa]:
            del pedidos[mesa][codigo]
            if len(pedidos[mesa]) == 0:
                del pedidos[mesa]
            print("Item removido.")
        else:
            print("Mesa ou produto não encontrado no pedido.")

    elif opcao == 6:
        mesa = int(input("Número da mesa: "))
        if mesa in pedidos:
            total = 0
            for codigo, qtd in pedidos[mesa].items():
                subtotal = cardapio[codigo]["preco"] * qtd
                total += subtotal
                print(f"{cardapio[codigo]['nome']} | {qtd} x R$ {cardapio[codigo]['preco']:.2f} = R$ {subtotal:.2f}")
            print(f"Total a pagar: R$ {total:.2f}")
        else:
            print("Essa mesa não possui pedidos.")

    elif opcao == 7:
        if len(pedidos) == 0:
            print("Nenhuma mesa com pedidos.")
        else:
            for mesa in pedidos:
                print(f"Mesa {mesa}")

    elif opcao == 8:
        print("Programa encerrado.")

    else:
        print("Opção inválida.")