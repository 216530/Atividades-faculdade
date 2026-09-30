'''
Leia um texto interativamente através da linha de comando
e retorna a contagem da ocorrência de cada letra do alfabeto no texto.
'''

# Passo 1: Ler o texto de forma interativa
texto = input("Digite um texto para contar as letras: ")

# Passo 2: Inicializar o dicionário vazio
contador_letras = {}

# Passo 3: Percorrer cada caractere do texto
for caractere in texto.lower():
    # Desconsiderar espaços, números e pontuações
    if caractere.isalpha():
        # Se a letra já estiver no dicionário, soma 1
        if caractere in contador_letras:
            contador_letras[caractere] += 1
        # Se for a primeira vez que a letra aparece, inicia com 1
        else:
            contador_letras[caractere] = 1

# Passo 4: Exibir os resultados de forma organizada
print("\nResultado da contagem:")
for letra, quantidade in sorted(contador_letras.items()):
    print(f"A letra '{letra}' apareceu: {quantidade}x")