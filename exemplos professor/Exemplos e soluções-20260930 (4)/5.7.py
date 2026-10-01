'''
Elaborar um algoritmo que leia 10 números
diferentes de zero. Para cada número lido,
o algoritmo deverá exibir uma mensagem
informando se o número é positivo ou negativo.
Caso o zero seja informado, este não deve ser
contado como uma leitura válida e uma mensagem
deve ser exibida ao usuário.
'''
conta = 0
while True :
    numero = int(input("Informe um valor: "))
    if numero > 0 :
        print("Numero positivo")
        conta += 1
    elif numero < 0 :
        print("Numero negativo")
        conta += 1
    else :
        print("Zero informado: invalido!")
    # condicao de parada
    if conta >= 10 :
        break



