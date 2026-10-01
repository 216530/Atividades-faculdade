'''
Em uma determinada cidade, a passagem escolar representa 60% do valor da
passagem normal. Cada estudante tem direito a adquirir até 50 passagens
escolares por mês letivo com desconto, podendo adquirir mais passagens,
mas sem o desconto. Desenvolva um algoritmo que receba o valor da passagem
normal e o número de passagens a serem adquiridas, calcule e apresente o
valor da passagem escolar e o montante a ser pago pelas passagens adquiridas.
'''
valor = float(input("Informe o valor da passagem normal: R$"))
quantidade = int(input("Informa quantidade a comprar: "))

if quantidade == 0 or valor == 0:
    print("Valor invalido")
    quit()

if quantidade > 50 :
    semDesconto = quantidade - 50
    total = (50 * valor * 0.6) + (semDesconto * valor)
else :
    total = (quantidade * valor * 0.6)
print("Total a pagar: ", total)
