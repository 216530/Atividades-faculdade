'''
1. Elabore uma aplicação para manter uma lista de compras utilizando a estrutura de conjuntos
com as seguintes funcionalidades:

a. adicionar item (se o item já estiver no conjunto, mostrar mensagem)
b. remover item
c. exibir todos os itens
d. ordernar o conjunto alfabeticamente
e. verificar se um item está contido em um conjunto
f. gravar a lista de compras em um arquivo (padrao lista.txt)
g. ler a lista de compras de um arquivo (padrao lista.txt)
'''
# variáveis

lista_compras = set()
arquivo_nome = "padraolista.txt"

while True:
    print("\n--- MENU DE COMPRAS ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir todos os itens")
    print("4. Ordenar alfabeticamente")
    print("5. Verificar item")
    print("6. Gravar em arquivo")
    print("7. Ler arquivo")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # estudar mais os métodos de string
        item = input("Digite o item: ").strip().capitalize()
        if item in lista_compras:
            print(f"O item '{item}' já está na lista!")
        else:
            lista_compras.add(item)
            print(f"'{item}' adicionado.")

    elif opcao == "2":
        item = input("Digite o item para remover: ").strip().capitalize()
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"'{item}' removido.")
        else:
            print("Item não encontrado.")

    elif opcao == "3":
        print("\nSua lista atual:")
        for i in lista_compras:
            print(f"- {i}")

    elif opcao == "4":
        # sorted() cria uma LISTA temporária. pq o conj não é ordenado e blablabla
        # lembrar de usar melhor o /n
        lista_ordenada = sorted(lista_compras)
        print("\nLista em ordem alfabética:")
        for i in lista_ordenada:
            print(f"- {i}")

    elif opcao == "5":
        item = input("Verificar qual item? ").strip().capitalize()
        if item in lista_compras:
            print(f"Sim, '{item}' está na lista.")
        else:
            print(f"Não, '{item}' não está na lista.")

    elif opcao == "6":
        # essa parte foi difícil, estudar mais depois, para não esquecer
        with open(arquivo_nome, "w") as arquivo:
            for item in lista_compras:
                arquivo.write(item + "\n")
        print("Gravado com sucesso em padraolista.txt")

    elif opcao == "7":
            with open(arquivo_nome, "r") as arquivo:
                for linha in arquivo:
                    # lembrar de remover \n do arquivo
                    lista_compras.add(linha.strip())
            print("Lista carregada do arquivo!")

    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida!")