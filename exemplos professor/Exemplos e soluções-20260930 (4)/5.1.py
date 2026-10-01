''' Desenvolva um algoritmo que exiba a tabuada
de um número qualquer escolhido pelo usuário '''

numero = int(input("Informe o numero da tabuada a exibir: "))
# repeticao de 10 vezes
for i in range(1, 11) :
    print(f"{i} x {numero} = { i * numero}")