'''
6. Desenvolva um algoritmo que leia números até que
a soma destes números seja maior do que 100. Ao final,
o algoritmo deverá exibir quantos números foram lidos até
que a condição de parada fosse atingida.
'''

soma = 0
contador = 0

while soma <= 100:
    num = int(input("Digite um número: "))
    
    soma += num
    contador += 1

print("Quantidade de números lidos:", contador)