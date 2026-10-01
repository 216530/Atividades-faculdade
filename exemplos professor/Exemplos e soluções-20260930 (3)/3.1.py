'''
Elabore um programa que lê o código do item pedido, a quantidade
e calcula o valor a ser pago pelo lanche. Considera que, a
cada execução, será solicitado apenas um item
'''
print("10 \tCachorro-quente \tR$1,10")
print("11 \tBauru simples \t\tR$1,30")
print("12 \tBauru com ovo \t\tR$1,50")
print("13 \tHamburguer \t\tR$1,10")
print("14 \tCheeseburger \t\tR$1,30")
print("15 \tRefrigerante \t\tR$1,50")
codigo = int(input("Informe codigo: "))

'''
match codigo :
    case 10 :
        valor = 1.1
    case 11 :
        valor = 1.3
    case 12 :
        valor = 1.5
    case 13 :
        valor = 1.1
    case 14 :
        valor = 1.3
    case 15 :
        valor = 1.5
    case other :
        print("Opcao inválida!")
        quit() # o mesmo que exit()
'''
match codigo :
    case 10 | 13:
        valor = 1.1
    case 11 | 14:
        valor = 1.3
    case 12 | 15 :
        valor = 1.5
    case other :
        print("Opcao inválida!")
        quit() # o mesmo que exit()

quantidade = int(input("Informe a quantidade: "))
print("Total: ", valor * quantidade)
        