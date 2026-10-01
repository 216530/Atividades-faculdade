''' Leia números inteiros até que uma condição de parada seja atingida.
Após, mostre-os. '''

numeros = []

while True :
    leitura = input("Informe um valor (fim para finalizar): ")
    
    # verifica condicao de parada
    if leitura.lower() == "fim" : 
        break
    
    # adiciona o valor lido ao final da lista
    numeros.append(int(leitura))

print(numeros)