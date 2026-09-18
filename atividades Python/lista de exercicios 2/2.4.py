''' 4. Leia 3 valores inteiros e diferentes e a seguir,
encontre e exiba o maior, o menor e o intermediário. '''

n1 = int(input("Informe um valor: "))
n2 = int(input("Informe um valor: "))
n3 = int(input("Informe um valor: "))


if n1 == n2 or n1 == n3 or n2 == n3 :
    print("Foram informados números iguais. Finalizando ...")
    exit(0)


if n1 > n2 and n1 > n3 :
    maior = n1
elif n2 > n1 and n2 > n3 :
    maior = n2
else :
    maior = n3


if n1 < n2 and n1 < n3 :
    menor = n1
elif n2 < n1 and n2 < n3 :
    menor = n2
else :
    menor = n3
    
intermediario = n1 + n2 + n3 - maior - menor
print(f"Maior: {maior} Menor: {menor} Meio: {intermediario}")


