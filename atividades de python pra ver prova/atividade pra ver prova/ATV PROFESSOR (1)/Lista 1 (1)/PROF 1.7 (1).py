'''
7. Leia um número correspondendo a uma quantidade de
dias e após, calcule e mostre a quantidade de anos,
meses e dias correspondentes. Para facilitar o cálculo,
considere ano com 365 dias e mês com 30 dias.
'''
leitura = int(input("Informe quantidade de dias: "))

anos = leitura // 365

print(leitura ," dias equivale a:")
print(anos, " anos")

resto = leitura % 365
meses = resto // 30
print(meses, " meses")

dias = resto % 30
print(dias, " dias")



