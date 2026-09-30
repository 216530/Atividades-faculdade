'''
5. Elabore um algoritmo que leia o nome e a idade de três pessoas
e após a leitura escreva o nome da pessoa mais velha e o nome da
pessoa mais nova. Considere que não existem idades iguais.
'''

nome1 = input("Digite o nome da 1ª pessoa: ")
idade1 = int(input("Digite a idade da 1ª pessoa: "))

nome2 = input("Digite o nome da 2ª pessoa: ")
idade2 = int(input("Digite a idade da 2ª pessoa: "))

nome3 = input("Digite o nome da 3ª pessoa: ")
idade3 = int(input("Digite a idade da 3ª pessoa: "))

# Descobrindo o mais velho
match idade1 > idade2 and idade1 > idade3:
    case True:
        mais_velho = nome1
    case False:
        match idade2 > idade1 and idade2 > idade3:
            case True:
                mais_velho = nome2
            case False:
                mais_velho = nome3

# Descobrindo o mais novo
match idade1 < idade2 and idade1 < idade3:
    case True:
        mais_novo = nome1
    case False:
        match idade2 < idade1 and idade2 < idade3:
            case True:
                mais_novo = nome2
            case False:
                mais_novo = nome3

print(f"Pessoa mais velha: {mais_velho}")
print(f"Pessoa mais nova: {mais_novo}")