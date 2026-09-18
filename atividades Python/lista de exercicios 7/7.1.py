#1. Elabore uma aplicação para manter uma lista de compras utilizando a 
#estrutura de conjuntos com as seguintes funcionalidades:
'''a. adicionar item (se o item já estiver no conjunto, mostrar mensagem)
b. remover item
c. exibir todos os itens
d. ordernar o conjunto alfabeticamente
e. verificar se um item está contido em um conjunto
f. gravar a lista de compras em um arquivo (padrao lista.txt)
g. ler a lista de comprar de um arquivo (padrao lista.txt)'''

#1. Elabore uma aplicação para manter uma lista de compras utilizando a 
#estrutura de conjuntos com as seguintes funcionalidades:
'''a. adicionar item (se o item já estiver no conjunto, mostrar mensagem)
b. remover item
c. exibir todos os itens
d. ordernar o conjunto alfabeticamente
e. verificar se um item está contido em um conjunto
f. gravar a lista de compras em um arquivo (padrao lista.txt)
g. ler a lista de comprar de um arquivo (padrao lista.txt)'''


compras = set()

while True:
    print("\n--- MENU LISTA DE COMPRAS ---")
    print("A - ADICIONAR ITEM")
    print("B - REMOVER ITEM")
    print("C - EXIBIR TODOS OS ITENS")
    print("D - EXIBIR ORDENADO ALFABETICAMENTE")
    print("E - VERIFICAR SE ITEM ESTÁ NA LISTA")
    print("F - GRAVAR LISTA EM ARQUIVO (lista.txt)")
    print("G - LER LISTA DE ARQUIVO (lista.txt)")
    print("ESCREVA 'FIM' PARA FINALIZAR")
    
    opcao = input("O que deseja fazer? ").upper()

    if opcao == "FIM":
        print("Programa finalizado!")
        break

    match opcao:
        case "A":
            item = input("O que você quer adicionar?: ")
            if item in compras:
                print(f"Aviso: O item '{item}' já está na lista!")
            else:
                compras.add(item)
                print(f"Item '{item}' adicionado com sucesso.")
        
        case "B":
            item = input("Qual item deseja remover?: ")
            if item in compras:
                compras.remove(item)
                print(f"Item '{item}' removido.")
            else:
                print("Erro: Item não encontrado na lista.")
        
        case "C":
            if not compras:
                print("A lista está vazia.")
            else:
                print("Itens na lista:")
                for item in compras:
                    print(f"- {item}")
        
        case "D":
            if not compras:
                print("A lista está vazia.")
            else:
                print("Itens ordenados:")
                # Conjuntos não têm ordem, então convertemos para lista para ordenar
                lista_ordenada = sorted(compras)
                for item in lista_ordenada:
                    print(f"- {item}")
        
        case "E":
            item = input("Qual item deseja verificar?: ")
            if item in compras:
                print(f"Sim, '{item}' está na lista.")
            else:
                print(f"Não, '{item}' não foi encontrado.")
        
        case "F":
            try:
                with open("lista.txt", "w", encoding="utf-8") as arquivo:
                    for item in compras:
                        arquivo.write(item + "\n")
                print("Lista gravada em 'lista.txt' com sucesso.")
            except Exception as e:  
                print(f"Erro ao gravar arquivo: {e}")
        
        case "G":
            try:
                with open("lista.txt", "r", encoding="utf-8") as arquivo:
                    # Lê as linhas, remove o \n e adiciona ao conjunto
                    # Isso limpa a lista atual ou adiciona a ela? 
                    # Geralmente ler de arquivo para um "set" de compras costuma substituir ou mesclar.
                    # Vou optar por adicionar à lista atual.
                    for linha in arquivo:
                        compras.add(linha.strip())
                print("Lista carregada de 'lista.txt' com sucesso.")
            except FileNotFoundError:
                print("Erro: O arquivo 'lista.txt' não existe.")
            except Exception as e:
                print(f"Erro ao ler arquivo: {e}")
        
        case _:
            print("Opção inválida!")
