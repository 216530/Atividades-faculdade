'''
3. Elaborar um algoritmo que lê 2 valores a e b, verifica
se são múltiplos um do outro e os escreve com a mensagem: São múltiplos
ou Não são múltiplos.
'''
#Variáveis
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

#Caso divida por 0
if a == 0 or b == 0:
    print("Não é possível verificar (divisão por zero)")
else:
    match a % b:
        case 0:
            print("São múltiplos")
        case _:
            match b % a:
                case 0:
                    print("São múltiplos")
                case _:
                    print("Não são múltiplos")