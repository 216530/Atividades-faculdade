'''
4. (Desafio) Escreva um algoritmo que retorne os números primos existentes entre 1 e 1000.
'''

for num in range(2, 1001):
    divisores = 0
    
    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1
    
    if divisores == 2:
        print(num)