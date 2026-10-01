''' Desenvolva um algoritmo que lê 5 números e
ao final, exibe a soma destes números.
'''
soma = 0
for x in range(5):
    soma += int(input(f"Informe o valor {x+1}: "))
    
print("Soma dos numeros: ", soma)
