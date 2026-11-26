import tkinter as tk
from tkinter import messagebox

def calcular(operacao):
    try:
        a = float(entrada_a.get().replace(",", "."))
        b = float(entrada_b.get().replace(",", "."))
    except ValueError:
        messagebox.showerror("Erro", "Informe números válidos.")
        return

    if operacao == "+":
        r = a + b
    elif operacao == "-":
        r = a - b
    elif operacao == "*":
        r = a * b
    else:
        if b == 0:
            messagebox.showerror("Erro", "Não é possível dividir por zero.")
            return
        r = a / b

    texto = f"{r:.4f}".rstrip("0").rstrip(".")
    resultado.config(text=f"Resultado: {texto}")

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("320x260")
janela.resizable(False, False)

tk.Label(janela, text="Primeiro número:").pack(pady=(15, 0))
entrada_a = tk.Entry(janela, width=25)
entrada_a.pack()

tk.Label(janela, text="Segundo número:").pack(pady=(10, 0))
entrada_b = tk.Entry(janela, width=25)
entrada_b.pack()

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=15)

for i, simbolo in enumerate(["+", "-", "*", "/"]):
    tk.Button(frame_botoes, text=simbolo, width=5,
              command=lambda s=simbolo: calcular(s)).grid(row=0, column=i, padx=4)

resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 13, "bold"))
resultado.pack(pady=10)

janela.mainloop()