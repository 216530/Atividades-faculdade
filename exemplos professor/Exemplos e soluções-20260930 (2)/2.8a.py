'''
Ler um valor em reais e mostrar qual o número de notas de 100, 50, 20, 10, 5 e 2 em que o valor lido pode ser decomposto.
Escrever o valor lido e a relação de notas necessárias.

Versao aprimorada
'''

# declaracao de variaveis
notas100 = notas50 = notas20 = notas10 = notas5 = notas2 = 0

valor = 901

if valor % 2 != 0:
    valor -= 5  # Retira uma nota de R$5 para tornar o valor par
    notas5 += 1
    
if valor % 10 == 8:  # Exemplo: 898 -> Retira três notas de R$2
    valor -= 6
    notas2 += 3
elif valor % 10 == 6:  # Exemplo: 896 -> Retira uma nota de R$2
    valor -= 2
    notas2 += 1    

notas100 += valor // 100
valor %= 100
print("Notas de R$100: ", notas100)

notas50 += valor // 50
valor %= 50
print("Notas de R$50: ", notas50)

notas20 += valor // 20
valor %= 20
print("Notas de R$20: ", notas20)

notas10 += valor // 10
valor %= 10
print("Notas de R$10: ", notas10)

notas5 += valor // 5
valor %= 5
print("Notas de R$5: ", notas5)

notas2 += valor // 2
print("Notas de R$2: ", notas2)
