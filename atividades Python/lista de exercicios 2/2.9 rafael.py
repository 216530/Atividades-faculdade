'''9. Calcule o imposto de renda de um contribuinte, onde o usuário informe o valor anual recebido e o 
sistema mostra o cálculo do imposto de renda de acordo com a tabela progressiva abaixo.

 Base de Cálculo Anual em R$ 	  Alíquota %  
Até 17.989,80	                     –
De 17.989,81 até 26.961,00	        7,5
De 26.961,01 até 35.948,40	        15,0
De 35.948,41 até 44.918,28	        22,5
Acima de 44.918,28	                27,5'''


valoranual = float(input("Informe seu valor anual recebido: "))

if valoranual <= 17989.80:
        aliquota = 0
elif valoranual <= 26961.40:
        aliquota = 7.5
elif valoranual <= 35948.40:
         aliquota = 15
elif valoranual <= 44918.28:
         aliquota = 22.5
else:
    aliquota = 27.5

imposto = valoranual * aliquota / 100
print(f"renda anual:R$ {valoranual}")
print(f"Valor Anual: {aliquota} % ")
print("imposto de renda: R$", round(imposto, 2))

     