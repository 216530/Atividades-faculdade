"""1. O cardápio de uma lancheria é o seguinte:

Cod	Descrição	Preço em R$
10	Cachorro-quente	1,10
11	Bauru simples	1,30
12	Bauru com ovo	1,50
13	Hamburguer	1,10
14	Cheeseburger	1,30
15	Refrigerante	1,50

Elabore um programa que lê o código do item pedido, a quantidade e calcula o valor a ser pago pelo lanche.
Considera que, a cada execução, será solicitado apenas um item."""

codigo = int(input("Digite o codigo do seu produto(10 - 15):"))

match codigo:
    case 10:
        quanti10 = int(input("Quantos cachorros quentes voce quer?"))
        valor = 1.10 * quanti10
        print(f"O seu pedido sera {quanti10} cachorros quentes por {valor}")
    case 11:
        quanti11 = int(input("Quantos Baurus simples voce quer?"))
        valor = 1.30 * quanti11
        print(f"O seu pedido sera {quanti11} Baurus Simples por R${valor}")
    case 12:
        quanti12 = int(input("Quantos Baurus com ovo voce quer?"))
        valor = 1.50 * quanti12
        print(f"O seu pedido sera {quanti12} Baurus com ovo por R${valor}")
    case 13:
        quanti13 = int(input("Quantos hamburguers voce quer?"))
        valor = 1.10 * quanti13
        print(f"O seu pedido sera {quanti13} hamburguers por R${valor}")
    case 14:
        quanti14 = int(input("Quantos chessburgers voce quer?"))
        valor = 1.30 * quanti14
        print(f"O seu pedido sera {quanti14} chessburguers por R${valor}")
    case 15:
        quanti15 = int(input("Quantos refrigerantes voce quer?"))
        valor = 1.50 * quanti15
        print(f"O seu pedido sera {quanti15} Refrigerantes por R${valor}")
