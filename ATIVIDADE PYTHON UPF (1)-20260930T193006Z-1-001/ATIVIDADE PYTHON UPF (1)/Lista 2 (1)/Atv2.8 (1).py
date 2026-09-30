'''
Ler um valor em reais e mostrar qual o número de notas de 100,
50, 20, 10, 5 e 2 em que o valor lido pode ser decomposto.
Escrever o valor lido e a relação de notas necessárias.
'''
#Variáveis

valor = int(input("Digite um valor em reais: "))

notas100 = valor // 100
valor = valor % 100

notas50 = valor // 50
valor = valor % 50

notas20 = valor // 20
valor = valor % 20

notas10 = valor // 10
valor = valor % 10

notas5 = valor // 5
valor = valor % 5

notas2 = valor // 2

print(f"{notas100} nota(s) de R$ 100")
print(f"{notas50} nota(s) de R$ 50")
print(f"{notas20} nota(s) de R$ 20")
print(f"{notas10} nota(s) de R$ 10")
print(f"{notas5} nota(s) de R$ 5")
print(f"{notas2} nota(s) de R$ 2")