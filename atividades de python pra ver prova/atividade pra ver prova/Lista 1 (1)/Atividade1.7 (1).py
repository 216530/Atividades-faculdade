'''
7. Leia um número correspondendo a uma quantidade de dias e após, calcule e mostre a quantidade de anos,
meses e dias correspondentes. Para facilitar o cálculo, considere ano com 365 dias e mês com 30 dias.
'''
#Variáveis

dias_total = int(input("Digite a quantidade de dias: "))
anos = dias_total // 365
resto = dias_total % 365
meses = resto // 30
dias = resto % 30

#Resultado

print("A quantidade em anos, meses e dias respectivamente é: ", anos, meses, dias)