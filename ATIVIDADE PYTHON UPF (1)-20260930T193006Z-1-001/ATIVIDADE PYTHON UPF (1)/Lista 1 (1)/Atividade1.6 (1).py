'''
6. Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada qual sendo
vendido respectivamente por 10, 12 e 15 reais. Implemente um programa em que o usuário
forneça a quantidade de camisetas pequenas,médias e grandes referentes a uma venda e
retorne o valor a ser cobrado.
'''

#Variáveis

camisetas_pequenas = float(input("Digite o número de camisetas pequenas vendidas: "))
camisetas_medias = float(input("Digite o número de camisetas médias vendidas: "))
camisetas_grandes = float(input("Digite o número de camisetas grandes vendidas: "))

#Conversão camiseta para dinheiro

conversaoP = camisetas_pequenas * 10
conversaoM = camisetas_medias * 12 + conversaoP
conversaoG = camisetas_grandes * 15 + conversaoM

#resultado
print("O valor total da compra: ", conversaoG)