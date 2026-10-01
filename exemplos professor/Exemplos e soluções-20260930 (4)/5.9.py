'''
9. Elabore um algoritmo que faça a média aritmética de qualquer
quantidade de números informada pelo usuário até que uma condição
de parada seja atingida. Mostrar a contagem de números informados
e a média.
'''
media = 0
conta = 0

while True :
    numero = int(input("Informe um número (zero para terminar): "))
    if numero == 0 :
        break
    media += numero
    conta += 1
print (f"Média: {media/conta} para {conta} números lidos")
