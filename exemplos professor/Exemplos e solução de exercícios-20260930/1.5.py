# Calcule a quantidade de cerveja, em litros, consumida por um bloco de carnaval.
# Para isso considere que uma garrafa de cerveja possui 600ml e uma caixa possui
# 24 garrafas. O algortimo deverá ler a quantidade de caixas consumidas e retornar
# a quantidade equivalente em litros.

caixas = int(input("Informe quantidade de caixas de cerveja: "))

litros = caixas * 24 * 0.6

print("Quantidade de litros: ", litros)
