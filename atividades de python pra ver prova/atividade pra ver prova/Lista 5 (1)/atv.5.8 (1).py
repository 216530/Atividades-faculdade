'''
8. Escreva um algoritmo para repetir a leitura de uma senha
até que ela seja válida. Para cada leitura da senha incorreta
informada escrever a mensagem "SENHA INVÁLIDA". Quanto a senha
for informada corretamente deve ser impressa a mensagem "ACESSO PERMITIDO"
e o algoritmo encerrado. Ao término do algoritmo exibir o número de leituras
efetuadas até que a senha correta fosse digitada. Considere que a senha correta é o valor 2023.
'''

contador = 0
senha = 0

while senha != 2023:
    senha = int(input("Digite a senha: "))
    contador += 1
    
    if senha != 2023:
        print("SENHA INVÁLIDA")

print("ACESSO PERMITIDO")
print("Número de tentativas:", contador)





