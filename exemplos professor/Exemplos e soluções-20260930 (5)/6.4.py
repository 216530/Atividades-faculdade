'''
Leia as quatro notas de 10 alunos, calcule e armazene em uma lista a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
'''
medias = []

for i in range(10) :
    print("Notas do aluno ", i+1)
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))
    nota4 = float(input("Informe a quarta nota: "))

    media = (nota1 + nota2 + nota3 + nota4)/4
    medias.append(media)

alunos = 0
for z in medias :
    if z >= 7 :
        alunos += 1
print(f"Houveram {alunos} com media igual ou superior a 7.0")