'''
Elabore um programa que lê o código do item pedido, a quantidade
e calcula o valor a ser pago pelo lanche. Considera que, a cada execução,
será solicitado apenas um item.
'''

print('Cod Descrição Preço em R$\n10 Cachorro-quente 1,10 \n11 Bauru simples 1,30 \n12 Bauru com ovo 1,50 \n13 Hamburguer 1,10 \n14 Cheeseburger 1,30 \n15 Refrigerante 1,50')

cod = int(input('Digite o código do produto:'))
quantidade = int(input('Digite a quantidade:'))

match cod:
    case 10:
        preço = 1.10
        print(f'{quantidade} Cachorro-quente(s), totalizando ', quantidade * preço)
    case 11:
        preço = 1.30 
        print(f'{quantidade} Bauru(s) simples, totalizando ', quantidade * preço)
    case 12:
        preço = 1.50 
        print(f'{quantidade} Bauru(s) com ovo, totalizando ', quantidade * preço)
    case 13:
        preço = 1.10 
        print(f'{quantidade} Hamburguer(es), totalizando ', quantidade * preço)
    case 14:
        preço = 1.30 
        print(f'{quantidade} Cheeseburger(es), totalizando ', quantidade * preço)
    case 15:
        preço = 1.50
        print(f'{quantidade} Refrigerante(s), totalizando ', quantidade * preço)
    case other:
        print('Produto não encontrado')