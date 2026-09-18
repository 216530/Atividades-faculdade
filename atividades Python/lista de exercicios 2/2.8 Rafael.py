'''8. Ler um valor em reais e mostrar qual o número de notas de 100, 50, 20, 10, 5 e 2
em que o valor lido pode ser decomposto. Escrever o valor lido e a relação de notas necessárias.'''

valor = int(input("digite o valor a sacar"))

n100 = valor // 100
resto = valor - (n100 * 100)

n50 = resto // 50
resto = resto - (n50 * 50)

n20 = resto // 20
resto = resto - (n20 * 20)

n10 = resto // 10
resto = resto - (n10 * 10)

n5 = resto // 5
resto = resto - (n5 * 5)

n2 = resto // 2
resto = resto - (n2 * 2)

print(f"Notas R$100: {n100}")
print(f"Notas R$50: {n50}")
print(f"Notas R$20: {n20}")
print(f"Notas R$10: {n10}")
print(f"Notas R$5: {n5}")
print(f"Notas R$2: {n2}")
print(resto)