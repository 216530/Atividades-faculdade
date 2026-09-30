'''
2. Demonstre com definir 2 conjuntos de números inteiros a seguir realizar as operações
fundamentais abaixo. Para saber mais sobre Conjuntos, consulte a Wikipedia sobre o Assunto.

a. união entre conjuntos
b. interseção entre conjuntos
c. diferença entre conjuntos
d. obter o tamanho do conjunto
e. obter o valor máximo e mínimo do conjunto

Após cada operação, apresente o conjunto resultante.
'''

# Variáveis
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

# União entre A e B
# Símbolo: barra reta vertical/pipe |
uniao = conjunto_a | conjunto_b
print(f"a. União (A | B): {uniao}")

# b. Interseção entre conjuntos (Apenas o que eles têm em comum)
# Símbolo: E comercial &
intersecao = conjunto_a & conjunto_b
print(f"b. Interseção (A & B): {intersecao}")

# c. Diferença entre conjuntos (O que tem no A que NÃO tem no B)
# Símbolo: menos -
diferenca = conjunto_a - conjunto_b
print(f"c. Diferença (A - B): {diferenca}")

# d. Obter o tamanho do conjunto
tamanho_a = len(conjunto_a)
print(f"d. Tamanho do Conjunto A: {tamanho_a} itens")

# e. Obter o valor máximo e mínimo
maximo_b = max(conjunto_b)
minimo_b = min(conjunto_b)
print(f"e. No Conjunto B: O valor máximo é {maximo_b} e o mínimo é {minimo_b}")