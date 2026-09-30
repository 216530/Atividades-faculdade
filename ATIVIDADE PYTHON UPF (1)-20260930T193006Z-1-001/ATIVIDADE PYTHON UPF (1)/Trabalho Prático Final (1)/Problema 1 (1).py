'''
Desenvolva um programa que receba uma quantidade de tempo
expressa em segundos e realize a conversão para horas, minutos e segundos.

O programa deverá solicitar ao usuário um número inteiro não negativo
correspondente ao total de segundos e calcular quantas horas completas,
quantos minutos completos e quantos segundos restantes estão contidos nesse valor.

Entrada
O programa deverá receber:

Um número inteiro maior ou igual a zero representando uma quantidade de segundos.
Saída
O programa deverá exibir:

A quantidade de horas;
A quantidade de minutos;
A quantidade de segundos restantes.
Exemplo
Entrada

6500
Saída

Horas: 1
Minutos: 48
Segundos: 20

Observações
Utilize operações de divisão inteira e cálculo de resto da divisão para obter os resultados.
Considere que 1 hora possui 3600 segundos e 1 minuto possui 60 segundos.
O programa deve funcionar para qualquer valor inteiro não negativo informado pelo usuário.
'''

import tkinter as tk

from tkinter import ttk

def converte():
    try:
        total_segundos = int(entrada.get())
        horas = total_segundos // 3600
        segundos_restantes = total_segundos % 3600
        minutos = segundos_restantes // 60
        segundos_finais = segundos_restantes % 60

        mensagem = f"Hora(s): {horas}\nMinuto(s): {minutos}\nSegundo(s): {segundos_finais}"

        label_resultado.config(text=mensagem)
        
    except ValueError:
        label_resultado.config(text="Por favor, digite apenas números inteiros!", fg="red")

janela = tk.Tk()
janela.title("Conversor")
janela.geometry("350x350")
janela.resizable(False, False)


tk.Label(janela, text="Coloque o total em segundos:").pack(pady=(10, 0))
entrada = tk.Entry(janela, width=25)
entrada.pack()

btn = tk.Button(
    janela,
    text="Converter",
    command=converte,
    width=15
)
btn.pack(pady=15)


label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=10)

janela.mainloop()
