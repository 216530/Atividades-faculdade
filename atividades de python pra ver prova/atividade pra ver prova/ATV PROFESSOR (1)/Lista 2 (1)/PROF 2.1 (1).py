# Leia um valor inteiro e em seguida apresenta uma mensagem se o número é PAR ou IMPAR.

valor = int( input("Informe um valor inteiro: ") )

if valor % 2 == 0 :
    print("Numero é PAR")
else :
    print("Numero é IMPAR")