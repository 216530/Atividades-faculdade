'''
Leia 3 valores inteiros e diferentes e a seguir, encontre
e exiba o maior, o menor e o intermediário.
'''

v1 = float(input("Informe primeiro valor: "))
v2 = float(input("Informe segundo valor: "))
v3 = float(input("Informe terceiro valor: "))

if v1 > v2 and v1 > v3 :
    maior = v1
elif v2 > v1 and v2 > v3 :
    maior = v2
elif v3 > v1 and v3 > v2 :
    maior = v3
    
if v1 < v2 and v1 < v3 :
    menor = v1
elif v2 < v1 and v2 < v3 :
    menor = v2
elif v3 < v1 and v3 < v2 :
    menor = v3

meio = (v1 + v2 + v3) - (maior + menor)

print("Valor maior: ", maior)
print("Valor menor: ", menor)
print("Valor intermediario: ", meio)