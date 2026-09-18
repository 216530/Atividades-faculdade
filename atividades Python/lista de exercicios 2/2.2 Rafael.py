''' 2. Leia dois valores inteiros e diferentes em seguida
apresenta o MAIOR e o MENOR número.'''

n1 = int(input("Informe primeiro valor: "))
n2 = int(input("Informe segundo valor: "))

if n1 == n2 :
    print("Valores informados são iguais")
elif n1 > n2 :
    print(f"{n1} maior que {n2}")
elif n1 < n2 :
    print(f"{n2} maior que {n1}")

