'''
Leia a idade de um nadador e a seguir classifique-o em
uma das seguintes categorias
'''

idade = int(input("Informe a idade do nadador: "))

if idade < 5 :
    categoria = "nao pode competir"
elif idade >= 5 and idade <= 7 :
    categoria = "infantil A"
elif idade >= 8 and idade <= 10 :
    categoria = "infantil B"
elif idade >= 11 and idade <= 13 :
    categoria = " juvenil A"
elif idade >= 14 and idade <= 17 :
    categoria = " juvenil B"
# elif idade > 18  :
else :
    categoria = " adulto"

print ("Categoria do nadador: ", categoria)
