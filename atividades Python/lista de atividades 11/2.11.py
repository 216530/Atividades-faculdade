import tkinter as tk
from tkinter import ttk, messagebox

alunos = [
    {
        "matricula": 1001,
        "nome": "Ana Silva",
        "curso": "Engenharia de Computação",
        "semestre": 3,
        "email": "ana@email.com"
    }
]

def atualizar_tabela():
    for item in tabela.get_children():
        tabela.delete(item)
    for a in alunos:
        tabela.insert("", "end", iid=str(a["matricula"]),
                      values=(a["matricula"], a["nome"], a["curso"], a["semestre"], a["email"]))

def cadastrar():
    try:
        matricula = int(entradas["matricula"].get())
        semestre = int(entradas["semestre"].get())
    except ValueError:
        messagebox.showerror("Erro", "Matrícula e semestre devem ser números inteiros.")
        return

    nome = entradas["nome"].get().strip()
    curso = entradas["curso"].get().strip()
    email = entradas["email"].get().strip()

    if not nome or not curso or not email:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return

    for a in alunos:
        if a["matricula"] == matricula:
            messagebox.showerror("Erro", "Já existe um aluno com essa matrícula.")
            return

    alunos.append({
        "matricula": matricula,
        "nome": nome,
        "curso": curso,
        "semestre": semestre,
        "email": email
    })

    for e in entradas.values():
        e.delete(0, tk.END)

    atualizar_tabela()

def excluir():
    selecionado = tabela.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um aluno para excluir.")
        return

    matricula = int(selecionado[0])
    if messagebox.askyesno("Confirmar", "Deseja excluir o aluno selecionado?"):
        for a in alunos:
            if a["matricula"] == matricula:
                alunos.remove(a)
                break
        atualizar_tabela()

janela = tk.Tk()
janela.title("Cadastro de Alunos")
janela.geometry("760x460")

frame_form = tk.Frame(janela)
frame_form.pack(pady=10)

campos = [("matricula", "Matrícula:"), ("nome", "Nome:"), ("curso", "Curso:"),
          ("semestre", "Semestre:"), ("email", "E-mail:")]

entradas = {}
for i, (chave, rotulo) in enumerate(campos):
    tk.Label(frame_form, text=rotulo).grid(row=i, column=0, sticky="e", padx=5, pady=3)
    entrada = tk.Entry(frame_form, width=35)
    entrada.grid(row=i, column=1, padx=5, pady=3)
    entradas[chave] = entrada

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=5)

tk.Button(frame_botoes, text="Cadastrar", width=12, command=cadastrar).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="Excluir", width=12, command=excluir).grid(row=0, column=1, padx=5)

colunas = ("matricula", "nome", "curso", "semestre", "email")
tabela = ttk.Treeview(janela, columns=colunas, show="headings", height=10)
for c, titulo, largura in [("matricula", "Matrícula", 80), ("nome", "Nome", 150),
                           ("curso", "Curso", 190), ("semestre", "Semestre", 70),
                           ("email", "E-mail", 190)]:
    tabela.heading(c, text=titulo)
    tabela.column(c, width=largura)
tabela.pack(padx=10, pady=10, fill="both", expand=True)

atualizar_tabela()
janela.mainloop()