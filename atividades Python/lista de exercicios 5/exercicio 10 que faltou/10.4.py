'''4. Cifra de César

Desenvolva um programa em Python que implemente a Cifra de César, 
técnica de criptografia que substitui cada letra de uma mensagem por outra, 
deslocada uma quantidade determinada de posições no alfabeto.

O programa deverá implementar duas funções:

    cifrar(mensagem, deslocamento): retorna a mensagem criptografada.
    decifrar(mensagem, deslocamento): retorna a mensagem original.

Implemente também um menu que permita ao usuário escolher entre cifrar uma mensagem, 
decifrar uma mensagem ou encerrar o programa.

Considere letras maiúsculas e minúsculas, 
preserve espaços e caracteres especiais e permita deslocamentos superiores a 26 posições. 
Não utilize bibliotecas prontas de criptografia.'''


palavra = "banana"
while True:
    # Exibição do Menu
    print("\n--- Criptografia irada ---")
    print("1. Cifrar palavra")
    print("2. Decifrar palavra")
    print("3. Sair")
    
    opcao = input("Escolha uma opção (1-3): ")

match:
    Case 1:
    letra = "b" 

