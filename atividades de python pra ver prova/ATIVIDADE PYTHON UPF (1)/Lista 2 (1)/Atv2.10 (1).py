'''
 Leia uma data informada pelo usuário (dia, mês e ano) e determine se aquela data é válida ou não.
 Uma data é considerada válida quando:

• O valor de ano está entre 0 e 3000.
• O valor de mês está entre 1 e 12
• O valor de dia:
– está entre 1 e 28 no mês de fevereiro em anos não bissextos.
– Está entre 1 e 29 no mês de fevereiro em anos bissextos.
– Está entre 1 e 30 nos meses de abril, junho, setembro e novembro.
– Está entre 1 e 31 nos demais casos. Leia uma data informada pelo usuário (dia, mês e ano) e
determine se aquela data é válida ou não. Uma data é considerada válida quando:

• O valor de ano está entre 0 e 3000.
• O valor de mês está entre 1 e 12
• O valor de dia:
– está entre 1 e 28 no mês de fevereiro em anos não bissextos.
– Está entre 1 e 29 no mês de fevereiro em anos bissextos.
– Está entre 1 e 30 nos meses de abril, junho, setembro e novembro.
– Está entre 1 e 31 nos demais casos.
'''
#Variáveis
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

# verificação do ano
if ano < 0 or ano > 3000:
    print("Data inválida")

# verificação do mês
elif mes < 1 or mes > 12:
    print("Data inválida")

else:
    # fevereiro
    if mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if 1 <= dia <= 29:
                print("Data válida")
            else:
                print("Data inválida")
        else:
            if 1 <= dia <= 28:
                print("Data válida")
            else:
                print("Data inválida")

    # meses com 30 dias
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if 1 <= dia <= 30:
            print("Data válida")
        else:
            print("Data inválida")

    # meses com 31 dias
    else:
        if 1 <= dia <= 31:
            print("Data válida")
        else:
            print("Data inválida")