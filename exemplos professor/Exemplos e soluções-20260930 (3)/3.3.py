'''
Elaborar um algoritmo que lê 2 valores a e b, verifica se são múltiplos
um do outro e os escreve com a mensagem: São múltiplos ou Não são múltiplos.
'''

a = int(input("Informe o valor a: "))
b = int(input("Informe o valor b: "))

if a % b == 0 :
    print("Sao multiplos")
else :
    print("Nao sao multiplos")
