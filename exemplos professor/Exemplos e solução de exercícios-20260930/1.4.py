'''
4. Leia a quotação do dólar do dia e uma
quantidade de Reais a ser convertida para
dólares. A final, exibir o valor correspondente
em dólares aos Reais informados.

'''
# lê a quotacao do dolar atual
dolar = float(input("Informe a quotação do Dólar de hoje: "))
reais = float(input("Informe valor em Reais para converter: "))

conversao = reais/dolar

#saída
print("Valor equivalente em Dólares: ", conversao)