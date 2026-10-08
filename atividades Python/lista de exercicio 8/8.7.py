def eh_palindromo(texto):
    limpo = "".join(c.lower() for c in texto if c.isalnum())
    return limpo == limpo[::-1]


frase = input("Digite uma palavra ou frase: ")

if eh_palindromo(frase):
    print("É um palíndromo")
else:
    print("Não é um palíndromo")