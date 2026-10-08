'''
Utilize os seguintes critérios para classificar o consumo do veículo:
Consumo Médio (km/l)                     Classificação
Maior ou igual a 14                      Excelente
Maior ou igual a 10 e menor que 14       Bom
Maior ou igual a 7 e menor que 10        Regular
Menor que 7                              Ruim

Entrada

O programa deverá receber:

    A distância percorrida em quilômetros (valor real);
    A quantidade de litros consumidos (valor real).

Saída

O programa deverá exibir:

    O consumo médio do veículo, com duas casas decimais;
    A classificação correspondente à eficiência do consumo.

Exemplo

Entrada

450
35.5

Saída

Consumo: 12.68 km/l
Classificação: Bom
'''

import tkinter as tk
from tkinter import messagebox


def calcular_consumo(distancia, combustivel):
    return distancia / combustivel

def classificar_eficiencia(consumo_medio):
    if consumo_medio >= 14:
        return "Excelente"
    elif consumo_medio >= 10:
        return "Bom"
    elif consumo_medio >= 7:
        return "Regular"
    else:
        return "Ruim"


def acao_botao_calcular():
    try:
        distancia = float(entry_distancia.get())
        combustivel = float(entry_combustivel.get())
        
        if combustivel == 0:
            messagebox.showerror("Erro", "A quantidade de combustível não pode ser zero!")
            return
            
        media = calcular_consumo(distancia, combustivel)
        classificacao = classificar_eficiencia(media)
        
        label_resultado_consumo.config(text=f"Consumo: {media:.2f} km/l")
        label_resultado_classificacao.config(text=f"Classificação: {classificacao}")
        
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, digite apenas números válidos.")


janela = tk.Tk()
janela.title("Calculadora de Consumo")
janela.geometry("300x250")  

label_distancia = tk.Label(janela, text="Distância percorrida (km):")
label_distancia.pack(pady=5)
entry_distancia = tk.Entry(janela)
entry_distancia.pack()

label_combustivel = tk.Label(janela, text="Combustível consumido (litros):")
label_combustivel.pack(pady=5)
entry_combustivel = tk.Entry(janela)
entry_combustivel.pack()

botao_calcular = tk.Button(janela, text="Calcular", command=acao_botao_calcular)
botao_calcular.pack(pady=15)

label_resultado_consumo = tk.Label(janela, text="Consumo: --", font=("Arial", 10, "bold"))
label_resultado_consumo.pack()

label_resultado_classificacao = tk.Label(janela, text="Classificação: --", font=("Arial", 10, "bold"))
label_resultado_classificacao.pack()

janela.mainloop()