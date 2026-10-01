'''
 Ler 3 valores inteiros. Verificar se estes valores não formam um triângulo,
 neste caso, mostrar mensagem de erro. Caso contrário, apresentar mensagem
 identificando o tipo do triângulo formado (isósceles, equilátero ou escaleno).
'''

a = int(input("Informe lado a do triangulo: "))
b = int(input("Informe lado b do triangulo: "))
c = int(input("Informe lado c do triangulo: "))

if (a + b) <= c or (b + c) <= a or (a + c) <= b :
    print("Nao forma triangulo")
    #return 0
    exit()
elif a == b and b == c :
    tipo = "Equilatero"
elif a != b and b != c and a != c :
    tipo = "Escaleno"
else :
    tipo = "Isosceles"
txt = "O triangulo [{},{},{}] é de tipo {}"
print(txt.format(a,b,c,tipo))
