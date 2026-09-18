inicial = int(input("informe o valor do intervalo: "))
final = int(input("informe o valor final do intervalo: "))

pares = "---Numero Pares---\n"
impares = "---Numero Impares---\n"
for i in (inicial, final):
    if i % 2 == 0:
        pares += str(i) + " "

for i in (inicial, final):
    if i % 2 != 0:
        impares += str(i) + " "

print(pares)
print(impares)