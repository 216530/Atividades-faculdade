'''
2. Desenvolva um algoritmo que lê 5 números e ao final, exibe a soma destes números.
'''

soma = 0
for x in range(5):
    num = int(input('Informe um valor:' ))
    soma += num #acumula numero na soma
    
print(soma)