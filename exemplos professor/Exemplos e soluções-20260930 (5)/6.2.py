''' Leia uma lista de 10 números de ponto flutuante e mostre-os na ordem inversa.'''
numeros = []
while len(numeros) < 10 :
    leitura = input("Informe um valor (fim para finalizar): ")
    
    # verifica se valor é numérico
    try:
      float(leitura)
    except:
      print("Valor digitado não é numérico! ")
      continue
    
    numeros.append(float(leitura))

numeros.reverse()
print(numeros)
    