'''

'''

usuarios = {}
id_user = 1

while True:
    print("1. Cadastrar (Create)")
    print("2. Visualizar (Read)")
    print("3. Atualizar (Update)")
    print("4. Excluir (Delete)")
    print("5. Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    match opcao:
        
        # Cadastrar
        
        case '1':
            print("\nCadastrar Novo Usuário")
            nome = input("Digite o nome: ")
            email = input("Digite o e-mail: ")
            idade = input("Digite a idade: ")
            
            usuarios[id_user] = {
                'nome': nome,
                'email': email,
                'idade': idade
            }
            print(f"Usuário '{nome}' cadastrado com o ID {id_user}.")
            id_user += 1

        
        # Ler
        
        case '2':
            print("\nLista de Usuários")
            if len(usuarios) == 0:
                print("Nenhum usuário cadastrado no momento.")
            else:
                for id_user, dados in usuarios.items():
                    print(f"ID: {id_user} | Nome: {dados['nome']} | E-mail: {dados['email']} | Idade: {dados['idade']}")

        
        # Atualizar
        
        case '3':
            print("\nAtualizar Usuário")
            id_busca = input("Digite o ID do usuário que deseja atualizar: ")
            
            if id_busca.isdigit():
                id_busca = int(id_busca)
                
                if id_busca in usuarios:
                    print(f"Atualizando os dados de: {usuarios[id_busca]['nome']}")
                    
                    novo_nome = input("Novo nome (pressione ENTER para manter atual): ")
                    novo_email = input("Novo e-mail (pressione ENTER para manter atual): ")
                    nova_idade = input("Nova idade (pressione ENTER para manter atual): ")
                    
                    if novo_nome != "":
                        usuarios[id_busca]['nome'] = novo_nome
                    if novo_email != "":
                        usuarios[id_busca]['email'] = novo_email
                    if nova_idade != "":
                        usuarios[id_busca]['idade'] = nova_idade
                        
                    print("Usuário atualizado com sucesso!")
                else:
                    print("Erro: Usuário não encontrado.")
            else:
                print("Erro: Por favor, digite um número de ID válido.")

        
        # Excluir
        
        case '4':
            print("\nExcluir Usuário")
            id_busca = input("Digite o ID do usuário que deseja excluir: ")
            
            if id_busca.isdigit():
                id_busca = int(id_busca)
                
                if id_busca in usuarios:
                    nome_excluido = usuarios[id_busca]['nome']
                    del usuarios[id_busca]
                    print(f"Usuário '{nome_excluido}' excluído com sucesso!")
                else:
                    print("Erro: Usuário não encontrado.")
            else:
                print("Erro: Por favor, digite um número de ID válido.")
                
        # Sair
        
        case '5':
            print("Encerrando o sistema... Até logo!")
            break
        
        # Caso digite num inválido
        
        case _:
            print("\nOpção inválida. Tente novamente.")