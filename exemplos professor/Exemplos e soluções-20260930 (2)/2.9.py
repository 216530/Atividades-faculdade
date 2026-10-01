'''
Calcule o imposto de renda de um contribuinte, onde o usuário informe o valor anual recebido e o
sistema mostra o cálculo do imposto de renda de acordo com a tabela progressiva abaixo.

Até 17.989,80	–
De 17.989,81 até 26.961,00	7,5
De 26.961,01 até 35.948,40	15,0
De 35.948,41 até 44.918,28	22,5
Acima de 44.918,28	27,5

'''
valorAnual = float(input("Informe o valor anual recebido: "))

if valorAnual <= 17989.80 :
    categoria = "Isento"
    ir = 0
elif valorAnual >= 17989.81 and valorAnual <= 26961.00 :
    categoria = "7.5%"
    ir = valorAnual * 0.075
elif valorAnual >= 26961.01 and valorAnual <= 35948.40 :
    categoria = "15%"
    ir = valorAnual * 0.15
elif valorAnual >= 35948.41 and valorAnual <= 44918.28 :
    categoria = "22.5%"
    ir = valorAnual * 0.225
else :
    categoria = "27.5%"
    ir = valorAnual * 0.275

txt = "Sua categoria de IR - {}, valor a pagar {}"
print(txt.format(categoria, ir))
