'''
 Elabore um algoritmo que leia o nome e a idade de três pessoas e após a leitura escreva o
 nome da pessoa mais velha e o nome da pessoa mais nova. Considere que não existem idades iguais.

'''

nome1 = input("Informe seu nome: ")
idade1 = int(input("Informe sua idade: "))
nome2 = input("Informe seu nome: ")
idade2 = int(input("Informe sua idade: "))
nome3 = input("Informe seu nome: ")
idade3 = int(input("Informe sua idade: "))


#classifica dados lidos
if idade1 > idade2 and idade1 > idade3 :
    idadeMaisVelha = idade1
    nomeMaisVelha = nome1
elif idade2 > idade1 and idade2 > idade3 :
    idadeMaisVelha = idade2
    nomeMaisVelha = nome2
else :
    idadeMaisVelha = idade3
    nomeMaisVelha = nome3

txt = "{}, é a pessoa mais velha com {} anos"
print(txt.format(nomeMaisVelha, idadeMaisVelha))