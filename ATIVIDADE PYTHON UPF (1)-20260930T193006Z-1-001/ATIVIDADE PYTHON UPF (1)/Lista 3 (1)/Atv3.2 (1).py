'''
2. Em uma determinada cidade, a passagem escolar representa 60%
do valor da passagem normal. Cada estudante tem direito a adquirir
até 50 passagens escolares por mês letivo com desconto, podendo adquirir
mais passagens, mas sem o desconto. Desenvolva um algoritmo que receba o
valor da passagem normal e o número de passagens a serem adquiridas, calcule
e apresente o valor da passagem escolar e o montante a ser pago pelas passagens adquiridas.
'''
#Variáveis
valor_normal = float(input("Digite o valor da passagem normal: "))
quantidade = int(input("Digite o número de passagens desejadas: "))

valor_escolar = valor_normal * 0.6

match quantidade:
    case 0:
        total = 0
    case 50:
        total = 50 * valor_escolar
    case _:
        if quantidade < 50:
            total = quantidade * valor_escolar
        else:
            com_desconto = 50 * valor_escolar
            sem_desconto = (quantidade - 50) * valor_normal
            total = com_desconto + sem_desconto

print(f"Valor da passagem escolar: R$ {valor_escolar}")
print(f"Total a pagar: R$ {total}")