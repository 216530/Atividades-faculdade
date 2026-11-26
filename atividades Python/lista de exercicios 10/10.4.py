'''Cifra de César
Desenvolva um programa em Python que implemente a Cifra de César, técnica de criptografia que substitui cada letra de uma mensagem por outra, deslocada uma quantidade determinada de posições no alfabeto.
O programa deverá implementar duas funções:

cifrar(mensagem, deslocamento): retorna a mensagem criptografada.
decifrar(mensagem, deslocamento): retorna a mensagem original.

Implemente também um menu que permita ao usuário escolher entre cifrar uma mensagem, decifrar uma mensagem ou encerrar o programa.
Considere letras maiúsculas e minúsculas, preserve espaços e caracteres especiais e permita deslocamentos superiores a 26 posições. Não utilize bibliotecas prontas de criptografia.
Referência: Cifra de César – Wikipédia.'''



def cifrar(mensagem, deslocamento):
    resultado = ""
    deslocamento = deslocamento % 26
    for letra in mensagem:
        if letra >= "A" and letra <= "Z":
            posicao = ord(letra) - ord("A")
            nova = (posicao + deslocamento) % 26
            resultado += chr(nova + ord("A"))
        elif letra >= "a" and letra <= "z":
            posicao = ord(letra) - ord("a")
            nova = (posicao + deslocamento) % 26
            resultado += chr(nova + ord("a"))
        else:
            resultado += letra
    return resultado


def decifrar(mensagem, deslocamento):
    resultado = ""
    deslocamento = deslocamento % 26
    for letra in mensagem:
        if letra >= "A" and letra <= "Z":
            posicao = ord(letra) - ord("A")
            nova = (posicao - deslocamento) % 26
            resultado += chr(nova + ord("A"))
        elif letra >= "a" and letra <= "z":
            posicao = ord(letra) - ord("a")
            nova = (posicao - deslocamento) % 26
            resultado += chr(nova + ord("a"))
        else:
            resultado += letra
    return resultado


opcao = 0
while opcao != 3:
    print("\n1 - Cifrar mensagem")
    print("2 - Decifrar mensagem")
    print("3 - Encerrar")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        texto = input("Digite a mensagem: ")
        desloc = int(input("Digite o deslocamento: "))
        print("Mensagem cifrada:", cifrar(texto, desloc))
    elif opcao == 2:
        texto = input("Digite a mensagem: ")
        desloc = int(input("Digite o deslocamento: "))
        print("Mensagem original:", decifrar(texto, desloc))
    elif opcao == 3:
        print("Programa encerrado.")
    else:
        print("Opção inválida.")