'''
2. Efetue a leitura de um texto a partir de um arquivo de entrada e apresenta
a contagem da ocorrência de cada palavra do texto fazendo uso da estrutura de dados dicionário.
'''

def abre_arquivo(arquivo):
    
    # abre arquivo em modo de leitura
    f = open(arquivo, "r", encoding="utf-8")
    
    return f

def conta_palavras(arquivoAberto):
    
    contagem = {}
    
    # itera sobre cada linha 
    for linha in arquivoAberto:
        
        # divide linha em palavras
        palavras = linha.split()
        
        # itera sobre cada palavra na lista
        for palavra in palavras:
            
            palavra = palavra.strip('\n').lower()
            
            # incrementa a contagem de palavras o dicionário
            contagem[palavra] = contagem.get(palavra, 0) + 1
            
    return contagem

a = abre_arquivo('luisfernandoverissimo.txt')

retorno = conta_palavras(a)

print('\n Contagem de palavras: ')
for chave, valor in retorno.items():
    print(f'{chave}: {valor} ocorrências')
