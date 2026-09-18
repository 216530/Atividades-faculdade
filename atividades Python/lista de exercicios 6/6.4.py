#4. Leia as quatro notas de 10 alunos, calcule e armazene 
# em uma lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias = []
for i in range(3):
    n1 = float(input("informe a nota 1 :"))
    n2 = float(input("informe a nota 2 :"))
    n3 = float(input("informe a nota 3 :"))
    n4 = float(input("informe a nota 4 :"))

medias.append((n1 + n2 + n3 + n4) /4)
conta = 0
for i in medias:
    if i >= 7:
        print(medias)
