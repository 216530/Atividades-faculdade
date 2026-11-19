tabuleiro = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]


def mostrar():
    print()
    print("     0   1   2")
    for i in range(3):
        print(" ", i, "", tabuleiro[i][0], "|", tabuleiro[i][1], "|", tabuleiro[i][2])
        if i < 2:
            print("    ---+---+---")
    print()


def verificar_vencedor(jogador):
    for i in range(3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False


def tabuleiro_cheio():
    for linha in tabuleiro:
        for casa in linha:
            if casa == " ":
                return False
    return True


print("=== JOGO DA VELHA ===")
jogador = "X"
jogadas = 0

while True:
    mostrar()
    print("Vez do jogador", jogador)

    try:
        linha = int(input("Linha (0 a 2): "))
        coluna = int(input("Coluna (0 a 2): "))
    except ValueError:
        print("Digite apenas numeros!")
        continue

    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        print("Posicao invalida! Use numeros de 0 a 2.")
        continue

    if tabuleiro[linha][coluna] != " ":
        print("Essa posicao ja esta ocupada!")
        continue

    tabuleiro[linha][coluna] = jogador
    jogadas += 1

    if verificar_vencedor(jogador):
        mostrar()
        print("Jogador", jogador, "venceu! Parabens!")
        break

    if tabuleiro_cheio():
        mostrar()
        print("Deu velha! Empate!")
        break

    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"
