'''
2. Efetue a leitura de um texto a partir de um arquivo de entrada
e apresenta a contagem da ocorrência de cada palavra do texto fazendo
uso da estrutura de dados dicionário.
'''


# Passo 1: Abrir e ler o arquivo de forma segura
# O 'with' garante que o arquivo será fechado automaticamente depois de lido
with open("texto.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# Passo 2: Inicializar o dicionário para as palavras
contador_palavras = {}

# Passo 3: Limpar o texto e dividir em palavras
# O .lower() padroniza e o .split() corta o texto nos espaços, gerando uma lista de palavras
palavras = conteudo.lower().split()

# Passo 4: Percorrer a lista de palavras
for palavra in palavras:
    # Remover pontuações coladas nas palavras (ex: "casa," vira "casa")
    palavra = palavra.strip(".,!?;:()\"'")
    
    # Se a palavra não estiver vazia (caso o texto tivesse apenas pontuação isolada)
    if palavra:
        # Se a palavra já existe no dicionário, soma 1
        if palavra in contador_palavras:
            contador_palavras[palavra] += 1
        # Se é a primeira vez que ela aparece, inicia com 1
        else:
            contador_palavras[palavra] = 1

# Passo 5: Exibir os resultados usando o .items() que vimos antes
print("\nContagem de palavras no arquivo:")
for palavra, quantidade in sorted(contador_palavras.items()):
    print(f"A palavra '{palavra}' aparece: {quantidade}x")