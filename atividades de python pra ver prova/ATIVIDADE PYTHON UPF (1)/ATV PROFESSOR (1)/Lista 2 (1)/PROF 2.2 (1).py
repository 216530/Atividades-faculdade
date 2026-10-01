# Leia dois valores inteiros e diferentes em seguida apresenta o MAIOR e o MENOR número.

valor1 = int(input("Informe primeiro valor: "))
valor2 = int(input("Informe segundo valor: "))

# testa se numeros sao diferentes
if valor1 == valor2 :
    print("Erro: valores sao iguais")
elif valor1 > valor2 :
    print("Primeiro valor é maior")
else :
    print("Segundo valor é maior")
    
