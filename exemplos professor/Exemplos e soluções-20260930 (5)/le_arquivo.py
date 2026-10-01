#  Leia um uma lista de 5 números inteiros e mostre-os.

f = open('lista.txt', 'r')
lista = []
for x in f.readlines(): 
    lista.append(x.replace("\n",""))

print(lista) 
f.close() 