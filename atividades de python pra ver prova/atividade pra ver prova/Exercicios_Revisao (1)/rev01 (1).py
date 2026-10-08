'''
    exemplo de ordenação usando a funcao sorted do python
    https://www.w3schools.com/python/ref_func_sorted.asp    
'''
def main():
    palavras = []
    print("Digite palavras. Para encerrar, digite 'fim'.\n")

    while True:
        palavra = input("Digite uma palavra: ").strip()
        if palavra.lower() == "fim":  # condição de parada
            break
        if palavra:  # evita adicionar string vazia
            palavras.append(palavra)

    # Ordenação pelo tamanho da palavra
    palavras_ordenadas = sorted(palavras, key=len)
    
    print("\nLista de palavras ordenadas pelo tamanho:")
    for p in palavras_ordenadas:
        print(f"{p} ({len(p)} caracteres)")

# execucao da funcao principal
main()
