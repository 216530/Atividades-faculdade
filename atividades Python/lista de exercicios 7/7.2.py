'''2. Demonstre com definir 2 conjuntos de números inteiros a seguir realizar as operações fundamentais abaixo. Para saber mais sobre Conjuntos, consulte a Wikipedia sobre o Assunto.

a. união entre conjuntos
b. interseção entre conjuntos
c. diferença entre conjuntos
d. obter o tamanho do conjunto
e. obter o valor máximo e mínimo do conjunto

Após cada operação, apresente o conjunto resultante.'''



A = {1,2,3,4,5}
B = {4,5,6,7,8}

print("Conjunto A:", A)
print("Conjunto B:", B)


uniao = A | B
print("União entre A e B:", uniao)

intersecao = A & B
print("Interseção entre A e B:", intersecao)

diferenca = A - B
print("Diferença entre A e B:", diferenca)

tamanho_A = len(A)
print("Tamanho do conjunto A:", tamanho_A)

tamanho_B = len(B)
print("Tamanho do conjunto B:", tamanho_B)

max_A = max(A)
min_A = min(A)
print("Máximo e mínimo do conjunto A:", max_A, min_A)

max_B = max(B)
min_B = min(B)
print("Máximo e mínimo do conjunto B:", max_B, min_B)