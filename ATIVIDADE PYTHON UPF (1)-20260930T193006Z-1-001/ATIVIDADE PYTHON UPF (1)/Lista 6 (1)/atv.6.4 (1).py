'''
4. Leia as quatro notas de 10 alunos, calcule e armazene em uma lista a média
de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
'''


medias = []

alunos_com_nota_boa = 0


for x in range(1, 11):
    soma_notas = 0
    print(f"\nDados do Aluno {x}:")
    
    
    for y in range(1, 5):
        nota = float(input(f"  Digite a {y}ª nota: "))
        soma_notas += nota 
    
    
    media_aluno = soma_notas / 4
    
    medias.append(media_aluno)
    
    
    if media_aluno >= 7.0:
        alunos_com_nota_boa += 1


print(f"Número de alunos com média >= 7.0: {alunos_com_nota_boa}")




