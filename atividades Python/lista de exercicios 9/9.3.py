'''3. Desenvolva um tradutor simples de língua estrangeira com as seguintes funcionalidades:

    incluir nova palavra e sua tradução
    alterar a tradução de uma palavra existente
    remover a palavra do dicionário
    traduzir (retornar a tradução associada com uma palavra)
    listar todas as palavras do dicionário e sua traduação.

Opcionalmente, implemente em sua aplicação a 
leitura de um arquivo de entrada e a saída em um outro arquivo traduzido com os 
termos encontrados no dicionário.'''


'''
3. Desenvolva um tradutor simples de língua estrangeira com as seguintes funcionalidades:

    incluir nova palavra e sua tradução
    alterar a tradução de uma palavra existente
    remover a palavra do dicionário
    traduzir (retornar a tradução associada com uma palavra)
    listar todas as palavras do dicionário e sua traduação.

'''

tradutor = {
    "apple": "maçã",
    "book": "livro",
    "computer": "computador"
}

while True:
    
    print("\n--- TRADUTOR SIMPLES (MATCH CASE) ---")
    print("1. Incluir nova palavra")
    print("2. Alterar tradução de uma palavra")
    print("3. Remover palavra")
    print("4. Traduzir palavra")
    print("5. Listar todo o dicionário")
    print("6. Sair")
    
    opcao = input("Escolha uma opção (1-6): ")

    match opcao:

        case "1":
            palavra = input("Digite a palavra em inglês: ").lower().strip()
            if palavra in tradutor:
                print(f"A palavra '{palavra}' já existe! Use a opção 2 para alterar.")
            else:
                traducao = input(f"Digite a tradução de '{palavra}': ").lower().strip()
                tradutor[palavra] = traducao
                print(f"'{palavra}' adicionada com sucesso!")

        
        case "2":
            palavra = input("Digite a palavra que deseja alterar: ").lower().strip()
            if palavra in tradutor:
                nova_traducao = input(f"Digite a nova tradução para '{palavra}': ").lower().strip()
                tradutor[palavra] = nova_traducao
                print(f"Tradução de '{palavra}' atualizada!")
            else:
                print(f"A palavra '{palavra}' não foi encontrada no dicionário.")

        case "3":
            palavra = input("Digite a palavra que deseja remover: ").lower().strip()
            if palavra in tradutor:
                del tradutor[palavra]
                print(f"A palavra '{palavra}' foi removida.")
            else:
                print(f"A palavra '{palavra}' não existe no dicionário.")

        case "4":
            palavra = input("Digite a palavra que quer traduzir: ").lower().strip()
            if palavra in tradutor:
                print(f"A tradução de '{palavra}' é: {tradutor[palavra]}")
            else:
                print(f"Desculpe, a palavra '{palavra}' não está no dicionário.")

    
        case "5":
            if not tradutor:
                print("O dicionário está vazio.")
            else:
                print("\n--- PALAVRAS NO DICIONÁRIO ---")
                for ingles, portugues in sorted(tradutor.items()):
                    print(f"{ingles} -> {portugues}")

        
        case "6":
            print("Saindo do tradutor. Até logo!")
            break
            
        
        case _:
            print("Opção inválida! Digite um número de 1 a 6.")