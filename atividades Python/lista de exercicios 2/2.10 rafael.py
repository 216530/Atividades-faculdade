'''10. Leia uma data informada pelo usuário (dia, mês e ano) e determine se aquela data é válida ou não. 
Uma data é considerada válida quando:

• O valor de ano está entre 0 e 3000.
• O valor de mês está entre 1 e 12
• O valor de dia:
– está entre 1 e 28 no mês de fevereiro em anos não bissextos.
– Está entre 1 e 29 no mês de fevereiro em anos bissextos.
– Está entre 1 e 30 nos meses de abril, junho, setembro e novembro.
– Está entre 1 e 31 nos demais casos.'''


dia = int(input("Digite o dia"))
mes = int(input("Digite o mes"))
ano = int(input("Digite o ano"))

datavalida = True

if ano < 0 or ano > 3000:
    datavalida = False
    
elif mes < 1 or mes > 12:
    datavalida = False

else:
    bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

if mes == 2:
    if bissexto:
        if dia < 1 or dia > 29:
            datavalida = False
    else:
        if dia < 1 or dia > 28:
            datavalida = False
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia < 1 or dia > 30:
        datavalida = False
else:
    if dia < 1 or dia > 31:
        datavalida = False
if datavalida:
    print("A data é valida!")
else:
    print("A data é invalida")