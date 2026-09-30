'''
7. Elaborar um algoritmo que leia 10 números diferentes de zero.
Para cada número lido, o algoritmo deverá exibir uma mensagem
informando se o número é positivo ou negativo. Caso o zero seja
informado, este não deve ser contado como uma leitura válida e
uma mensagem deve ser exibida ao usuário.
'''

contador = 0

while contador < 10:
    num = int(input("Digite um número diferente de zero: "))
    
    if num == 0:
        print("Zero não é válido! Digite outro número.")
    else:
        contador += 1
        
        if num > 0:
            print("Número positivo")
        else:
            print("Número negativo")