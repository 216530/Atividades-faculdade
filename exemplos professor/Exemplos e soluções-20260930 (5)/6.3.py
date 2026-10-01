''' Leia uma lista de 10 caracteres, e diga quantas consoantes foram
lidas. Imprima-as. '''

caracteres = []
consoantes = []
conta = 0

for i in range(10):
    c = input("Informe um caractere :")
    caracteres.append(c[0])

# classifica caracteres lidos
for i in caracteres :
    if i.lower() not in ('a', 'e', 'i', 'o', 'u') and i.isalpha():
        consoantes.append(i.lower())
        conta += 1

print(f"Caracteres lidos: {caracteres}")
print(f"Consoantes: [{conta}] : {consoantes}")
