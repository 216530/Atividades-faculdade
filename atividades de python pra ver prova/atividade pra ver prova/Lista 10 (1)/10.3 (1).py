'''
 3. Elabore um programa que implementa o Jogo da Velha

utilizando uma matriz de elementos 3 x 3 para armazenar as

jogadas.

'''


def exibir_tabuleiro(tabuleiro):
    print()
    print(f" {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} ")
    print("---|---|---")
    print(f" {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} ")
    print("---|---|---")
    print(f" {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} ")
    print()


def verificar_vencedor(tab):
    # Linhas
    for i in range(3):
        if tab[i][0] == tab[i][1] == tab[i][2]:
            return True
    # Colunas
    for j in range(3):
        if tab[0][j] == tab[1][j] == tab[2][j]:
            return True
    # Diagonais
    if tab[0][0] == tab[1][1] == tab[2][2]:
        return True
    if tab[0][2] == tab[1][1] == tab[2][0]:
        return True
        
    return False


def jogar_velha():
    
    tabuleiro = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    
    jogador_atual = "X"
    jogadas = 0
    ganhou = False
    
    
    while jogadas < 9 and not ganhou:
        exibir_tabuleiro(tabuleiro)
        
        
        escolha = input(f"Jogador {jogador_atual}, escolha um espaço.\n")
        
        
        jogada_valida = False
        for linha in range(3):
            for coluna in range(3):
                if tabuleiro[linha][coluna] == escolha:
                    tabuleiro[linha][coluna] = jogador_atual
                    jogada_valida = True
                    
        if jogada_valida:
            jogadas += 1
            ganhou = verificar_vencedor(tabuleiro)
            
            
            if not ganhou:
                if jogador_atual == "X":
                    jogador_atual = "O"
                else:
                    jogador_atual = "X"
        else:
            print("Espaço inválido ou já ocupado! Tente novamente.")
            
    
    exibir_tabuleiro(tabuleiro)
    print("-------------------")
    if ganhou:
        print(f"Fim de jogo! O Jogador {jogador_atual} venceu!")
    else:
        print("Fim de jogo! Deu Velha (empate)!")


jogar_velha()