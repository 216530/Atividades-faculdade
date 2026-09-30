'''
Calcule o imposto de renda de um contribuinte, onde o usuário
informe o valor anual recebido e o sistema mostra o cálculo do
imposto de renda de acordo com a tabela progressiva abaixo.

 Base de Cálculo Anual em R$    Alíquota %  
Até 17.989,80 –
De 17.989,81 até 26.961,00       7,5
De 26.961,01 até 35.948,40       15,0
De 35.948,41 até 44.918,28       22,5
Acima de 44.918,28 27,5
'''

renda = float(input("Digite a renda anual: "))

if renda <= 17989.80:
    imposto = 0

elif renda <= 26961.00:
    imposto = renda * 0.075

elif renda <= 35948.40:
    imposto = renda * 0.15

elif renda <= 44918.28:
    imposto = renda * 0.225

else:
    imposto = renda * 0.275

print("Imposto de renda:", imposto)