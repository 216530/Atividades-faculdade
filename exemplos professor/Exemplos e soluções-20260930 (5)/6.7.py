'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre
um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente".
'''

perguntas = [ "Telefonou para a vítima?",
              "Esteve no local do crime?",
              "Mora perto da vítima?",
              "Devia para a vítima?",
              "Já trabalhou com a vítima?" ]

respostas = list()
conta = 0

# recebe respostas
for i in range (len(perguntas)) :
    respostas.append(input(perguntas[i]+"(s/n): "))

# classificar o status da pessoa
for i in range (len(respostas)) :
    if respostas[i] in ['S','s'] :
        conta += 1
if conta < 2 :
    status = 'inocente'
elif conta < 3 :
    status = 'suspeito'
elif conta <= 4 :
    status = 'cumplice'
else : # elif conta == 5
    status = 'culpado'

#print("Seu status no crime é: ", status)
print(f"Seu status no crime é: {status}")
              


