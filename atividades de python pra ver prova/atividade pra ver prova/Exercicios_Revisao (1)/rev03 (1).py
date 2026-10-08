estoque = {
}

while True:
    print("\n===== MENU =====")
    print("1. Adicionar item")
    print("2. Remover item do estoque")
    print("3. Listar itens")
    print("4. Consultar item")
    print("5. Sair")

    opc = input("Escolha uma opção: ")

    if opc == "1":
        item = input("Item a adicionar: ").lower()
        qtd = int(input("Quantidade: "))
        if qtd < 0:
            print("Quantidade inválida!")
            continue
        estoque[item] = estoque.get(item, 0) + qtd
        print("Item adicionado/atualizado!")

    elif opc == "2":
        item = input("Item a remover: ").lower()
        if item not in estoque:
            print("Item não encontrado!")
            continue
        qtd = int(input("Quantidade a remover: "))
        if qtd < 0 or qtd > estoque[item]:
            print("Quantidade inválida!")
            continue
        estoque[item] -= qtd
        print("Item atualizado!")
        if estoque[item] == 0:
            del estoque[item]

    elif opc == "3":
        print("\nEstoque atual:")
        for k, v in estoque.items():
            print(f"{k}: {v}")

    elif opc == "4":
        item = input("Item para consultar: ").lower()
        print(f"{item}: {estoque.get(item, 'Item não existe')}")

    elif opc == "5":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
