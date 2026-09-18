lista1 = []
lista2 = []
lista3 = []

for i in range(10):
    valor = input(f"Digite o valor{i+1} para lista 1: ")
    lista1.append(valor)

for i in range(10):
    valor = input(f"Digite o valor{i+1} para lista 2: ")
    lista2.append(valor)

for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(f"lista 1 {lista1}")
print(f"lista 2 {lista2}")
print(f"lista 3 {lista3}")