'''
Desenvolva um programa que receba um número inteiro positivo e determine se ele é um número primo.

Um número primo é um número natural maior que 1 que possui exatamente
dois divisores distintos: o número 1 e ele próprio. Portanto, números primos não podem
ser divididos exatamente por nenhum outro valor além desses dois.

O programa deverá analisar o número informado pelo usuário e
indicar se ele é ou não um número primo.
Entrada

O programa deverá receber:

    Um número inteiro positivo.

Saída

O programa deverá exibir uma das seguintes mensagens:

    Primo
    Não é primo

Exemplos

Entrada

17

Saída

Primo

Entrada

1

Saída

Não é primo

Entrada

2

Saída

Primo

Entrada

15

Saída

Não é primo

Observações

Considere que o número 1 não é primo.
O programa deverá verificar se existem divisores além de 1 e do próprio número.
Para melhorar a eficiência da solução, recomenda-se realizar as verificações
apenas até a raiz quadrada do número.
Implemente uma função denominada eh_primo(n) responsável por determinar
se o número é primo ou não.
Utilize o módulo math para obter a raiz quadrada do número durante a verificação.

Requisitos

    Utilizar estruturas de repetição para testar os possíveis divisores.
    Utilizar estruturas condicionais para determinar o resultado.
    Organizar a lógica de verificação em uma função específica.

'''

import tkinter as tk
from tkinter import messagebox
import math


def eh_primo(n):
    if n <= 1:
        return False
    
    limite = int(math.sqrt(n)) + 1
    
    for i in range(2, limite):
        if n % i == 0:
            return False 
            
    return True 


def acao_botao_verificar():
    try:
        numero = int(entry_numero.get())
        
        if numero < 0:
            messagebox.showerror("Erro de Validação", "Por favor, digite um número positivo.")
            return
            
        if eh_primo(numero):
            resultado = "Primo"
        else:
            resultado = "Não é primo"
            
        label_resultado.config(text=f"Resultado: {resultado}")
        
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, digite apenas um número inteiro válido.")


janela = tk.Tk()
janela.title("Verificador de Números Primos")
janela.geometry("300x220")

label_numero = tk.Label(janela, text="Digite um número inteiro positivo:", font=("Arial", 10))
label_numero.pack(pady=10)
entry_numero = tk.Entry(janela, font=("Arial", 10), justify="center") # texto centralizado
entry_numero.pack()

botao_verificar = tk.Button(janela, text="Verificar se é Primo", command=acao_botao_verificar, font=("Arial", 10, "bold"), bg="#9C27B0", fg="white")
botao_verificar.pack(pady=15)

label_resultado = tk.Label(janela, text="Resultado: --", font=("Arial", 12, "bold"))
label_resultado.pack(pady=5)

janela.mainloop()