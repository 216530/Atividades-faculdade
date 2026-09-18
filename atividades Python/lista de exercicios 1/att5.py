#5. Calcule a quantidade de cerveja, em litros, consumida por um bloco de carnaval.
#Para isso considere que uma garrafa de cerveja possui 600ml e uma caixa possui 24 garrafas.
#O algortimo deverá ler a quantidade de caixas consumidas
#e retornar a quantidade equivalente em litros

caixas = int(input('informe quantidade de caixas consumidas '))

litros= caixas * 0.6 * 24

print(f'{caixas} caixas equivalem a {litros} litros')
