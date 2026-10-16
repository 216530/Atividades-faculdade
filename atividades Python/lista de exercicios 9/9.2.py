def contar_palavras(arquivo):

    contagem_palavras = {}

    f = open(arquivo, 'r', encoding="utf-8")  

    for linha in f:
        palavras = linha.split()

        for palavra in palavras:
            palavra = palavra.split('\n').lower()
            contagem_palavras[palavra] = contagem_palavras.get(palavra , 0) + 1
    return contagem_palavras

def main():
    arquivo = input("Digite o caminho do arquivo de texto: ")

    try:
        contagem_palavras_resultado = contar_palavras(arquivo)
        for palavra, contagem in contagem_palavras_resultado.items():
            print(f"{palavra}: {contagem}")
    except FileNotFoundError:
        print("arquivo nao encontrado")