'''
Leia duas listas com 10 elementos cada. Gere um terceira lista de
20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados das duas outras listas.
'''

lista1 = list()
lista2 = list()
uniao = list()

print("Lendo lista 1")
for i in range(0,10) :
    lista1.append(input("Informe item: "))

print("Lendo lista 2")
for i in range(0,10) :
    lista2.append(input("Informe item: "))

for i in range(0,10) :
    uniao.append(lista1[i])
    uniao.append(lista2[i])
    
print("Lista intercalada resultante:\n", uniao)
