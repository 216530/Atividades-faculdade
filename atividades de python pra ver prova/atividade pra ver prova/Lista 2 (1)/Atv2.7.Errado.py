'''
Ler 3 valores inteiros. Verificar se estes valores não formam um triângulo,
neste caso, mostrar mensagem de erro. Caso contrário, apresentar mensagem
identificando o tipo do triângulo formado (isósceles, equilátero ou escaleno).
'''

ang1 = int(input('Informe o primeiro ângulo interno:'))
ang2 = int(input('Informe o segundo ângulo interno:'))
ang3 = int(input('Informe o terceiro ângulo interno:'))

if ang1 + ang2 + ang3 != 180:
    print('Não é um triângulo')
else:
    if (ang1 == ang2 and ang1 != ang3) or (ang1 == ang3 and ang1 != ang2) or (ang2 == ang3 and ang2 != ang1):
        print('Triângulo ISÓSCELES')
    if ang1 == ang2 and ang1 == ang3 and ang2 == ang3:
        print('Triângulo EQUILÁTERO')
    if ang1 != ang2 and ang1 != ang3 and ang2 != ang3:
        print('Triângulo ESCALENO')