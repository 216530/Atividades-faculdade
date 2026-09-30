'''
Desenvolva um programa que receba as medidas dos três lados de uma figura geométrica
e determine se elas podem formar um triângulo. Caso o triângulo seja válido,
o programa deverá identificar e informar sua classificação.

Para que três segmentos formem um triângulo, é necessário que a soma de quaisquer dois
lados seja sempre maior que o terceiro lado.
Regra de Validade

Um triângulo é considerado válido quando:

    lado A + lado B > lado C
    lado A + lado C > lado B
    lado B + lado C > lado A

Se qualquer uma dessas condições não for satisfeita, os valores informados não formam um triângulo.
Classificação dos Triângulos

Caso o triângulo seja válido, ele deverá ser classificado conforme as regras abaixo:
Tipo 	Descrição
Equilátero 	Os três lados possuem a mesma medida
Isósceles 	Exatamente dois lados possuem a mesma medida
Escaleno 	Os três lados possuem medidas diferentes
Entrada

O programa deverá receber:

    A medida do lado A (valor real);
    A medida do lado B (valor real);
    A medida do lado C (valor real).

Saída

O programa deverá exibir uma das seguintes mensagens:

    Não é triângulo
    Equilátero
    Isósceles
    Escaleno

Exemplo

Entrada

3
4
5

Saída

Escaleno

Exemplo 2

Entrada

5
5
5

Saída

Equilátero

Exemplo 3

Entrada

2
3
8

Saída

Não é triângulo

Observações

    Considere que os valores informados representam medidas positivas.
    O programa deve verificar inicialmente a validade do triângulo antes de realizar sua classificação.
    Utilize estruturas condicionais para implementar as verificações necessárias.
Desenvolva um programa que receba as medidas dos três lados de uma figura geométrica e determine se elas podem formar um triângulo. Caso o triângulo seja válido, o programa deverá identificar e informar sua classificação.

Para que três segmentos formem um triângulo, é necessário que a soma de quaisquer dois lados seja sempre maior que o terceiro lado.
Regra de Validade

Um triângulo é considerado válido quando:

    lado A + lado B > lado C
    lado A + lado C > lado B
    lado B + lado C > lado A

Se qualquer uma dessas condições não for satisfeita, os valores informados não formam um triângulo.
Classificação dos Triângulos

Caso o triângulo seja válido, ele deverá ser classificado conforme as regras abaixo:
Tipo 	Descrição
Equilátero 	Os três lados possuem a mesma medida
Isósceles 	Exatamente dois lados possuem a mesma medida
Escaleno 	Os três lados possuem medidas diferentes
Entrada

O programa deverá receber:

    A medida do lado A (valor real);
    A medida do lado B (valor real);
    A medida do lado C (valor real).

Saída

O programa deverá exibir uma das seguintes mensagens:

    Não é triângulo
    Equilátero
    Isósceles
    Escaleno

Exemplo

Entrada

3
4
5

Saída

Escaleno

Exemplo 2

Entrada

5
5
5

Saída

Equilátero

Exemplo 3

Entrada

2
3
8

Saída

Não é triângulo

Observações

    Considere que os valores informados representam medidas positivas.
    O programa deve verificar inicialmente a validade do triângulo antes de realizar sua classificação.
    Utilize estruturas condicionais para implementar as verificações necessárias.

'''

import tkinter as tk
from tkinter import messagebox


def eh_triangulo_valido(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

def classificar_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"


def acao_botao_verificar():
    try:
        lado_a = float(entry_a.get())
        lado_b = float(entry_b.get())
        lado_c = float(entry_c.get())
        
        if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
            messagebox.showerror("Erro", "As medidas devem ser valores maiores que zero!")
            return

        if eh_triangulo_valido(lado_a, lado_b, lado_c):
            resultado = classificar_triangulo(lado_a, lado_b, lado_c)
        else:
            resultado = "Não é triângulo"
            
        label_resultado.config(text=f"Resultado: {resultado}")
        
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, digite apenas números válidos.")


janela = tk.Tk()
janela.title("Verificador de Triângulos")
janela.geometry("300x320")

# Lado A
label_a = tk.Label(janela, text="Medida do Lado A:", font=("Arial", 10))
label_a.pack(pady=3)
entry_a = tk.Entry(janela, font=("Arial", 10))
entry_a.pack()

# Lado B
label_b = tk.Label(janela, text="Medida do Lado B:", font=("Arial", 10))
label_b.pack(pady=3)
entry_b = tk.Entry(janela, font=("Arial", 10))
entry_b.pack()

# Lado C
label_c = tk.Label(janela, text="Medida do Lado C:", font=("Arial", 10))
label_c.pack(pady=3)
entry_c = tk.Entry(janela, font=("Arial", 10))
entry_c.pack()

botao_verificar = tk.Button(janela, text="Verificar Triângulo", command=acao_botao_verificar, font=("Arial", 10, "bold"), bg="#2196F3", fg="white")
botao_verificar.pack(pady=15)

label_resultado = tk.Label(janela, text="Resultado: --", font=("Arial", 12, "bold"))
label_resultado.pack(pady=5)

janela.mainloop()