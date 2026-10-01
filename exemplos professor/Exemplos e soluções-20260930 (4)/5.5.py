'''
5. Desenvolva um algoritmo que leia 10 números e ao
final da leitura, mostre quantos, dos números lidos
são positivos e quantos são negativos.
'''
positivos = 0
negativos = 0

for i in range(10) :
    numero = int(input(f"Informe o valor[{i+1}]:  "))
    if numero > 0 :
        positivos += 1
    elif numero < 0 :
        negativos += 1
    else :
        print("Informado zero")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

    
