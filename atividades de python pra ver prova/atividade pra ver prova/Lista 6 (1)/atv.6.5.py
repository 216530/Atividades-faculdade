'''
5. Leia duas listas com 10 elementos cada. Gere um terceira lista de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados das duas outras listas.
'''

lista1 = []
lista2 = []

lista3 = []

# Primeira lista
print("Dados da Lista 1:")
for i in range(10):
    item = input(f"  Digite o {i+1}º elemento: ")
    lista1.append(item)

# Segunda lista
print("\nDados da Lista 2:")
for i in range(10):
    item = input(f"  Digite o {i+1}º elemento: ")
    lista2.append(item)


for i in range(10):
    
    lista3.append(lista1[i])
    
    lista3.append(lista2[i])

print(lista3)

