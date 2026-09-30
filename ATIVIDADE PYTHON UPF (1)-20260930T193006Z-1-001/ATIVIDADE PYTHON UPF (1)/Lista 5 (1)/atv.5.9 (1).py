'''
9. Elabore um algoritmo que faça a média aritmética de qualquer
quantidade de números informada pelo usuário até que uma condição
de parada seja atingida. Mostrar a contagem de números informados e a média.
'''

soma = 0
contador = 0

num = int(input("Digite um número (0 para parar): "))

while num != 0:
    soma += num
    contador += 1
    
    num = int(input("Digite um número (0 para parar): "))

if contador > 0:
    media = soma / contador
    print("Quantidade de números:", contador)
    print("Média:", media)
else:
    print("Nenhum número válido foi digitado.")