''' 5. Leia a idade de um nadador e a seguir classifique-o em uma
das seguintes categorias:
 infantil A	 5 - 7 anos 
 infantil B  8-10 anos
 juvenil A 	 11-13 anos 
 juvenil B 	 14-17 anos 
 adulto	 maiores de 18 anos '''

idade = int(input("Informe a idade: "))
# classifica o nadador
if idade < 5 :
    print("não categorizado")
elif idade <= 7 :
    print("infantil A")
elif idade <= 10 :
    print("infantil B")
elif idade <= 13 :
    print("juvenil A")
elif idade <= 17 :
    print("juvenil B")
elif idade >= 18 :
    print("adulto")
    
