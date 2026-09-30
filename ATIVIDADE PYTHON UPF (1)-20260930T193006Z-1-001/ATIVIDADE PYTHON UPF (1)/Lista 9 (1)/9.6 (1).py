'''
6. Desenvolva uma aplicação para controle de estoque de produtos com os seguintes dados:
código do produto, nome, quantidade em estoque e preço e funcionalidades CRUD, com leitura
e gravação em arquivo no formato JSON.
'''
import json

def carregar_estoque(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

def salvar_estoque(estoque, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(estoque, arquivo, indent=4)

def adicionar_produto(estoque, codigo, nome, quantidade):
    if codigo in estoque:
        print("Este código de produto já está em uso.")
    else:
        estoque[codigo] = {'nome': nome, 'quantidade': quantidade}
        print("Produto adicionado ao estoque.")

def atualizar_estoque(estoque, codigo, quantidade):
    if codigo in estoque:
        estoque[codigo]['quantidade'] += quantidade
        
        print("Quantidade atualizada com sucesso.")
    else:
        print("Produto não encontrado no estoque.")
        
        
def main():
    arquivo_estoque = 'estoque.json'
    estoque = carregar_estoque(arquivo_estoque)
    
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar Produto")
        print("2. Atualizar Estoque")
        print("3. Exibir Estoque")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            codigo = input("Digite o código do produto: ")
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade do produto: "))
            adicionar_produto(estoque, codigo, nome, quantidade)
            
        elif opcao == '2':
            codigo = input("Digite o código do produto: ")
            quantidade = int(input("Digite a quantidade a ser adicionada/somada: "))
            atualizar_estoque(estoque, codigo, quantidade)
            
        elif opcao == '3':
            if not estoque:
                print("O estoque está vazio.")
            else:
                print("\n--- Produtos no Estoque ---")
                for codigo, dados in estoque.items():
                    print(f"Código: {codigo} | Nome: {dados['nome']} | Quantidade: {dados['quantidade']}")
                    
        elif opcao == '4':
            salvar_estoque(estoque, arquivo_estoque)
            print("Estoque salvo com sucesso. Saindo...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

main()