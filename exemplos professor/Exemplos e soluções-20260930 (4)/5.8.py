'''
8. Escreva um algoritmo para repetir a leitura de uma
senha até que ela seja válida. Para cada leitura da senha
incorreta informada escrever a mensagem "SENHA INVÁLIDA". Quanto
a senha for informada corretamente deve ser impressa a mensagem
"ACESSO PERMITIDO" e o algoritmo encerrado. Ao término do algoritmo
exibir o número de leituras efetuadas até que a senha correta fosse
digitada. Considere que a senha correta é o valor 2023.
'''
senha = '2023'
conta = 0
while True :
    leitura = input("Informe a senha: ")
    conta += 1
    if senha == leitura :
        print(f"Acesso permitido, após {conta} leituras!")
        break
    else :
        print("Senha inválida!")
        