#2. Leia uma lista de 10 números de ponto flutuante e mostre-os na ordem inversa.

numeros = []
while len(numeros) < 10 :
    leitura = input("informe os valores a serem adicionados a lista.(0  pra finalizar):")
    if leitura.isnumeric():
        numeros.append(float(leitura))
    else:
        print("valor digitado não é numerico!")
numeros.reverse()
print(numeros)