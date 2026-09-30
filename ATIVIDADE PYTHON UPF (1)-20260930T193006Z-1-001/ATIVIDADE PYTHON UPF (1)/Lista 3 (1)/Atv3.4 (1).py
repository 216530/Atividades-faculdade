'''
4. Desenvolva um algoritmo que leia o nome de uma pessoa,
o dia e o mês de seu nascimento e sem seguida apresente o
nome da pessoa e o seu signo conforme a tabela abaixo:
Signo       Período
Aquário     21/1 - 18/2
Peixes      19/2 - 20/3
Áries       21/3 - 20/4
Touro       21/4 - 21/5
Gêmeos      22/5 - 21/6
Câncer      22/6 - 22/7
Leão        23/7 - 23/8
Virgem      24/8 - 22/9
Libra       23/9 - 23/10
Escorpião   24/10 - 22/11
Sagitário   23/11 - 21/12
Capricórnio 22/12 - 20/1
'''

nome = input("Digite seu nome: ")
dia = int(input("Digite o dia do nascimento: "))
mes = int(input("Digite o mês do nascimento: "))

match mes:
    case 1:
        signo = "Capricórnio" if dia <= 20 else "Aquário"
    case 2:
        signo = "Aquário" if dia <= 18 else "Peixes"
    case 3:
        signo = "Peixes" if dia <= 20 else "Áries"
    case 4:
        signo = "Áries" if dia <= 20 else "Touro"
    case 5:
        signo = "Touro" if dia <= 21 else "Gêmeos"
    case 6:
        signo = "Gêmeos" if dia <= 21 else "Câncer"
    case 7:
        signo = "Câncer" if dia <= 22 else "Leão"
    case 8:
        signo = "Leão" if dia <= 23 else "Virgem"
    case 9:
        signo = "Virgem" if dia <= 22 else "Libra"
    case 10:
        signo = "Libra" if dia <= 23 else "Escorpião"
    case 11:
        signo = "Escorpião" if dia <= 22 else "Sagitário"
    case 12:
        signo = "Sagitário" if dia <= 21 else "Capricórnio"
    case _:
        signo = "Mês inválido"

print(f"{nome}, seu signo é {signo}.")