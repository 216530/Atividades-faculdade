'''
2. Leia uma lista de 10 números de ponto flutuante e mostre-os na ordem inversa.
'''

numsList = []

for x in range(11):
    nums = float(input('Escreva 10 números que tenham pelo menos 1 casa após a vírgula: '))
    
    numsList.append(nums)
    
    
numsList.reverse()
print(f'Você digitou esses números: ', numsList)