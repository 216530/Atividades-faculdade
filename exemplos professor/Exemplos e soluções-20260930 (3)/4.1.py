txt = "abcdefghijklmnopqrstuvWXYZ01234567890!@#$%ˆ&*()abc"
# txt = input("Informe uma sequencia de caracteres: ")

#1 A quantidade ou contagem de caracteres que formam a String
print(len(txt));

#2 O primeiro e o último caractere
print(txt[0], txt[len(txt)-1])
# ou
print(txt[0], txt[-1])

#3 O caracter na posição ___ a partir do início da String
print(txt[10:11])
# ou
print(txt[10])

#4 O caracter na posição ___ a partir do final da String
print(txt[-3:-2])

#5 A String convertida em maiúsculas
print(txt.upper())

#6 A String convertida em minúsculas
print(txt.lower())

#7 A String com todos os caracteres __ substituídos por __
print(txt.replace("abc","123"))

#8 Separar cada palavra que forma a frase "A ligeira raposa
# marrom ataca o cão preguiçoso". Quantas palavras formam
# esta frase ?
frase = "A ligeira raposa marrom ataca o cão preguiçoso"
palavras = frase.split(" ")
print(frase.split(" "))
print(len(frase.split(" ")))
print(palavras[1])

#9 Verifique se a sequência de caracteres ___ encontra-se na String lida
buscar = "raposa"
print(frase.find(buscar))

if (buscar in frase) :
    print("Encontrado")
else :
    print("Nao Encontrado")

#10 Concatenar os caracteres "==" ao início e ao final da String lida
txt = "==" + txt + "=="
print(txt)

#11 Contar o número de vezes que o caracteres ___ ocorre na String lida
print(txt.count("a"))

#12 Retornar a posição em uma String onde se encontra o caractere ___
print(txt.index("W"))

#13 Retornar se a String e composta unicamente de caracteres alfabéticos
print(txt.isalpha())
print("abcdefgh".isalpha())

#14 Retornar se a String e composta unicamente de caracteres numéricos
print(txt.isdigit())
print("12345".isdigit())

#15 Retornar a String formato de título (cada palavra com a inicial em maiúscula)
print(frase.title())





