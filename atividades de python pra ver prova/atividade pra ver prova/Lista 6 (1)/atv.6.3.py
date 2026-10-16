'''
3. Leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas. Imprima-as.
'''
caracteres = []

consoantes = []

vogais = "aeiou"

print("Por favor, digite 10 caracteres(minúsculos):")

for i in range(10):
    char = input(f"Digite o {i+1}º caractere: ")
    
    caracteres.append(char)
    
    if char.isalpha() and char not in vogais:
        consoantes.append(char)

print(f"As consoantes são: {consoantes}")