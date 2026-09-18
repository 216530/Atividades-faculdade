#3. Leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas. Imprima-as
letras = []
consoantes = []
conta = 0
for i in range(10):
    c = input("informe um caractere: ")
    letras.append(c[0])


    for i in letras:
        if i.lower() not in('a','e','i','o','u') and i.isalpha():
            consoantes.append(i.lower())
            conta += 1
print(f"caracteres lidos :{letras}")
print(f"consoates: [{conta}] : {consoantes}")