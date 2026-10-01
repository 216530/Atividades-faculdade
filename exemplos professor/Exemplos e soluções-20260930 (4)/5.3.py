''' Escreva um algoritmo que lê dois números e em seguida exibe
os números pares e os números ímpares existentes entre estes dois números.
'''

inicial = int(input("Informe valor inicial do intervalo: "))
final = int(input("Informe valor final do intervalo: "))

pares = "--- Números pares ---\n"
impares = "--- Números impares ---\n"

# gera os pares intermediarios do intervalo
for i in range(inicial+1, final) :
    if i % 2 == 0 :
        pares += str(i) + " "
# gera os impares intermediarios do intervalo
for i in range(inicial+1, final) :
    if i % 2 != 0 :
        impares += str(i) + " "       
print(pares)
print(impares)        
        
