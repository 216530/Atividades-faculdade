'''
 Desenvolva um algoritmo que leia o nome de uma pessoa, o dia e o mês de seu nascimento e em
 seguida apresente o nome da pessoa e o seu signo conforme a tabela 

'''

nome = input("Informe seu nome: ")
dia = int(input("Informe dia de nascimento [1-31]: "))
mes = int(input("Informe mes de nascimento [1-12]: "))

# converte dia/mes para escala numérica
mesdia = (mes * 100) + dia

if mesdia <= 120 :
    signo = "Capricornio"
elif mesdia >= 121 and mesdia <= 218 :
    signo = "Aquário"
elif mesdia >= 219 and mesdia <= 320 :
    signo = "Peixes"
elif mesdia >= 321 and mesdia <= 420 :
    signo = "Áries"
elif mesdia >= 421 and mesdia <= 521 :
    signo = "Touro"
elif mesdia >= 522 and mesdia <= 621 :
    signo = "Gemeos"
elif mesdia >= 622 and mesdia <= 722 :
    signo = "Cancer"
elif mesdia >= 723 and mesdia <= 823 :
    signo = "Leao"
elif mesdia >= 824 and mesdia <= 922 :
    signo = "Virgem"
elif mesdia >= 923 and mesdia <= 1023 :
    signo = "Libra"
elif mesdia >= 1024 and mesdia <= 1122 :
    signo = "Escorpiao"
elif mesdia >= 1123 and mesdia <= 1221 :
    signo = "Sagitário"
elif mesdia >= 1222 :
    signo = "Capricornio"
    
txt = "{}, seu signo é {}"
print(txt.format(nome, signo))