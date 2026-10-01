'''
Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande,
cada qual sendo vendido respectivamente por 10, 12 e 15 reais. Implemente
um programa em que o usuário forneça a quantidade de camisetas pequenas,
médias e grandes referentes a uma venda e retorne o valor a ser cobrado.
'''

p = int(input("Informe quantidade de camisetas P a adquirir: "))
m = int(input("Informe quantidade de camisetas M a adquirir: "))
g = int(input("Informe quantidade de camisetas G a adquirir: "))

total = (p * 10) + (m * 12) + (g * 15)

print("Total a pagar: R$", total)