import random

palavras = ["python", "banco", "dados", "sistema", "rede", "teclado", "monitor",
            "programa", "internet", "algoritmo", "variavel", "funcao", "servidor"]

palavra = random.choice(palavras)
acertadas = []
erradas = []
max_erros = 5

desenhos = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========="""
]

print("=== JOGO DA FORCA ===")

while True:
    print(desenhos[len(erradas)])

    mostrar = ""
    for letra in palavra:
        if letra in acertadas:
            mostrar += letra + " "
        else:
            mostrar += "_ "
    print("\nPalavra:", mostrar)
    print("Letras erradas:", ", ".join(erradas))
    print("Erros:", len(erradas), "de", max_erros)

    if "_" not in mostrar:
        print("\nParabens! Voce ganhou! A palavra era", palavra)
        break

    if len(erradas) == max_erros:
        print("\nVoce foi enforcado! A palavra era", palavra)
        break

    letra = input("\nDigite uma letra: ").lower().strip()

    if len(letra) != 1 or not letra.isalpha():
        print("Digite apenas uma letra!")
        continue

    if letra in acertadas or letra in erradas:
        print("Voce ja tentou essa letra!")
        continue

    if letra in palavra:
        acertadas.append(letra)
        print("Acertou!")
    else:
        erradas.append(letra)
        print("Errou!")
