''' 1. Leia um valor inteiro e em seguida apresenta uma
mensagem se o número é PAR ou IMPAR. '''

valor = int(input("Digite um valor: "))

if valor == 0 :
    print("Informado zero!")
elif valor < 0 :
    print("Informado valor negativo!")
elif valor % 2 == 0 :
    print(f"{valor} é par")
else :
    print(f"{valor} é impar")