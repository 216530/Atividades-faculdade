def ordena(palavras):
    """
    Ordena a lista pelo tamanho das palavras
    usando o algoritmo Selection Sort 
    """
    n = len(palavras)

    for i in range(n):
        indice_menor = i

        for j in range(i + 1, n):
            if len(palavras[j]) < len(palavras[indice_menor]):
                indice_menor = j

        # Troca os elementos
        palavras[i], palavras[indice_menor] = palavras[indice_menor], palavras[i]

    return palavras

def main():
    palavras = []
    print("Digite palavras. Para encerrar, digite 'fim'.\n")
    while True:
        palavra = input("Digite uma palavra: ").strip()
        if palavra.lower() == "fim":
            break
        if palavra:
            palavras.append(palavra)

    # Ordenação manual (Selection Sort)
    palavras_ordenadas = ordena(palavras[:])  # usar cópia

    print("\nPalavras ordenadas por tamanho:")
    for p in palavras_ordenadas:
        print(f"{p} ({len(p)} caracteres)")

# execucao do metodo principal
main()
