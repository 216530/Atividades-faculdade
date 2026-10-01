'''
Desenvolva um programa que avalie o desempenho de um time em um campeonato a partir da
quantidade de vitórias, empates e derrotas obtidas.

O programa deverá calcular a pontuação total conquistada pela equipe,
determinar seu aproveitamento percentual e classificar seu desempenho
conforme critérios pré-estabelecidos.

Sistema de Pontuação

Considere a seguinte regra de pontuação:
Resultado  Pontos
Vitória  3 pontos
Empate   1 ponto
Derrota  0 pontos

Cálculo do Aproveitamento

O aproveitamento percentual deverá ser calculado pela fórmula:

Aproveitamento (%) = (Pontos Obtidos ÷ Pontos Possíveis) × 100

Onde:

    Pontos Obtidos = (Vitórias × 3) + (Empates × 1)
    Pontos Possíveis = Número de Jogos × 3
    Número de Jogos = Vitórias + Empates + Derrotas

Classificação do Desempenho

Utilize os seguintes critérios para classificar o desempenho da equipe:
Aproveitamento                        Classificação
Maior ou igual a 70%                  Excelente
Maior ou igual a 50% e menor que 70%  Bom
Maior ou igual a 30% e menor que 50%  Regular
Menor que 30%                         Ruim

Entrada

O programa deverá receber:

    Quantidade de vitórias (número inteiro);
    Quantidade de empates (número inteiro);
    Quantidade de derrotas (número inteiro).

Saída

O programa deverá exibir:

    A pontuação total obtida;
    O aproveitamento percentual com duas casas decimais;
    A classificação do desempenho.

Exemplo

Entrada

8
3
5

Saída

Pontos: 27
Aproveitamento: 56.25%
Classificação: Bom

Exemplo 2

Entrada

12
4
2

Saída

Pontos: 40
Aproveitamento: 74.07%
Classificação: Excelente

Observações

    Considere que os valores informados são números inteiros não negativos.
    O programa deverá calcular inicialmente a pontuação total e o número de jogos disputados.
    Apresente o aproveitamento com duas casas decimais.
    Recomenda-se organizar os cálculos em funções para tornar o código mais modular e reutilizável.

'''
import tkinter as tk
from tkinter import messagebox


def calcular_pontuacao(vitorias, empates):
    return (vitorias * 3) + (empates * 1)

def calcular_aproveitamento(pontos_obtidos, total_jogos):
    if total_jogos == 0:
        return 0.0
    
    pontos_possiveis = total_jogos * 3
    porcentagem = (pontos_obtidos / pontos_possiveis) * 100
    return porcentagem

def classificar_desempenho(aproveitamento):
    if aproveitamento >= 70:
        return "Excelente"
    elif aproveitamento >= 50:
        return "Bom"
    elif aproveitamento >= 30:
        return "Regular"
    else:
        return "Ruim"


def acao_botao_analisar():
    try:
        vitorias = int(entry_vitorias.get())
        empates = int(entry_empates.get())
        derrotas = int(entry_derrotas.get())
        
        if vitorias < 0 or empates < 0 or derrotas < 0:
            messagebox.showerror("Erro de Validação", "As quantidades não podem ser negativas!")
            return
            
        total_jogos = vitorias + empates + derrotas
        pontos = calcular_pontuacao(vitorias, empates)
        aproveitamento = calcular_aproveitamento(pontos, total_jogos)
        classificacao = classificar_desempenho(aproveitamento)
        
        label_resultado_pontos.config(text=f"Pontos: {pontos}")
        label_resultado_aproveitamento.config(text=f"Aproveitamento: {aproveitamento:.2f}%")
        label_resultado_classificacao.config(text=f"Classificação: {classificacao}")
        
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, digite apenas números inteiros válidos.")


janela = tk.Tk()
janela.title("Desempenho do Time")
janela.geometry("320x340")

label_vitorias = tk.Label(janela, text="Quantidade de Vitórias:", font=("Arial", 10))
label_vitorias.pack(pady=3)
entry_vitorias = tk.Entry(janela, font=("Arial", 10))
entry_vitorias.pack()

label_empates = tk.Label(janela, text="Quantidade de Empates:", font=("Arial", 10))
label_empates.pack(pady=3)
entry_empates = tk.Entry(janela, font=("Arial", 10))
entry_empates.pack()

label_derrotas = tk.Label(janela, text="Quantidade de Derrotas:", font=("Arial", 10))
label_derrotas.pack(pady=3)
entry_derrotas = tk.Entry(janela, font=("Arial", 10))
entry_derrotas.pack()

botao_analisar = tk.Button(janela, text="Analisar Desempenho", command=acao_botao_analisar, font=("Arial", 10, "bold"))
botao_analisar.pack(pady=15)

label_resultado_pontos = tk.Label(janela, text="Pontos: --", font=("Arial", 11, "bold"))
label_resultado_pontos.pack(pady=2)

label_resultado_aproveitamento = tk.Label(janela, text="Aproveitamento: --", font=("Arial", 11, "bold"))
label_resultado_aproveitamento.pack(pady=2)

label_resultado_classificacao = tk.Label(janela, text="Classificação: --", font=("Arial", 11, "bold"))
label_resultado_classificacao.pack(pady=2)

janela.mainloop()