'''
5. Escreva uma função Python que recebe um vetor de inteiros de qualquer
tamanho e informe se os elementos do array estão classificados em ordem
crescente, ou seja, ordenados do menor para o maior. A função deverá retornar
um valor true ou false.
'''



def esta_em_ordem(vetor):
    if vetor == sorted(vetor):
        return True
    else:
        return False

print(esta_em_ordem([1, 2, 3, 5, 8])) # True
print(esta_em_ordem([1, 5, 3, 4, 8])) # False