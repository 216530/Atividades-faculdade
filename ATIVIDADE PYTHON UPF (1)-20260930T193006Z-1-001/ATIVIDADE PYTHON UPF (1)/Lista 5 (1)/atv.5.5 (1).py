'''
5. Desenvolva um algoritmo que leia 10 números e ao
final da leitura, mostre quantos, dos números lidos
são positivos e quantos são negativos.
'''

nums = [10, -5, 2, -11, 31, -17, 5, -20, 3, -1, 4]

positivos = 0
negativos = 0

for x in nums:
    if x > 0:
        positivos += 1
    elif x < 0:
        negativos += 1

print(f'Quantidade de positivos: {positivos}')
print(f'Quantidade de negativos: {negativos}')