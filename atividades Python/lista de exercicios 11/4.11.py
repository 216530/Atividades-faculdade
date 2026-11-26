import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

tarefas = []
proximo_codigo = 1

def atualizar():
    for item in tabela.get_children():
        tabela.delete(item)

    filtro = combo_filtro.get()
    for t in tarefas:
        if filtro == "Todas" or t["situacao"] == filtro:
            tabela.insert("", "end", iid=str(t["codigo"]),
                          values=(t["codigo"], t["descricao"], t["vencimento"], t["prioridade"], t["situacao"]))

    pendentes = sum(1 for t in tarefas if t["situacao"] == "Pendente")
    concluidas = len(tarefas) - pendentes
    lbl_contagem.config(text=f"Pendentes: {pendentes}   |   Concluídas: {concluidas}")

def cadastrar():
    global proximo_codigo

    descricao = entrada_descricao.get().strip()
    vencimento = entrada_vencimento.get().strip()
    prioridade = combo_prioridade.get()

    if not descricao:
        messagebox.showerror("Erro", "Informe a descrição da tarefa.")
        return

    try:
        datetime.strptime(vencimento, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Erro", "Informe a data no formato dd/mm/aaaa.")
        return

    tarefas.append({
        "codigo": proximo_codigo,
        "descricao": descricao,
        "vencimento": vencimento,
        "prioridade": prioridade,
        "situacao": "Pendente"
    })
    proximo_codigo += 1

    entrada_descricao.delete(0, tk.END)
    entrada_vencimento.delete(0, tk.END)
    combo_prioridade.set("Média")
    atualizar()

def tarefa_selecionada():
    selecionado = tabela.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione uma tarefa.")
        return None
    codigo = int(selecionado[0])
    for t in tarefas:
        if t["codigo"] == codigo:
            return t

def concluir():
    t = tarefa_selecionada()
    if t:
        t["situacao"] = "Concluída"
        atualizar()

def excluir():
    t = tarefa_selecionada()
    if t and messagebox.askyesno("Confirmar", "Deseja excluir a tarefa selecionada?"):
        tarefas.remove(t)
        atualizar()

janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.geometry("740x470")

frame_form = tk.Frame(janela)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Descrição:").grid(row=0, column=0, sticky="e", padx=5, pady=3)
entrada_descricao = tk.Entry(frame_form, width=40)
entrada_descricao.grid(row=0, column=1, columnspan=3, padx=5, pady=3, sticky="w")

tk.Label(frame_form, text="Vencimento:").grid(row=1, column=0, sticky="e", padx=5, pady=3)
entrada_vencimento = tk.Entry(frame_form, width=14)
entrada_vencimento.grid(row=1, column=1, padx=5, pady=3, sticky="w")

tk.Label(frame_form, text="Prioridade:").grid(row=1, column=2, sticky="e", padx=5, pady=3)
combo_prioridade = ttk.Combobox(frame_form, values=["Baixa", "Média", "Alta"], state="readonly", width=10)
combo_prioridade.set("Média")
combo_prioridade.grid(row=1, column=3, padx=5, pady=3)

tk.Button(frame_form, text="Cadastrar", width=12, command=cadastrar).grid(row=2, column=1, pady=8, sticky="w")

frame_acoes = tk.Frame(janela)
frame_acoes.pack(pady=5)

tk.Button(frame_acoes, text="Marcar como concluída", command=concluir).grid(row=0, column=0, padx=5)
tk.Button(frame_acoes, text="Excluir", command=excluir).grid(row=0, column=1, padx=5)

tk.Label(frame_acoes, text="Filtrar:").grid(row=0, column=2, padx=(20, 5))
combo_filtro = ttk.Combobox(frame_acoes, values=["Todas", "Pendente", "Concluída"], state="readonly", width=12)
combo_filtro.set("Todas")
combo_filtro.grid(row=0, column=3)
combo_filtro.bind("<<ComboboxSelected>>", lambda e: atualizar())

colunas = ("codigo", "descricao", "vencimento", "prioridade", "situacao")
tabela = ttk.Treeview(janela, columns=colunas, show="headings", height=10)
for c, titulo, largura in [("codigo", "Código", 60), ("descricao", "Descrição", 260),
                           ("vencimento", "Vencimento", 100), ("prioridade", "Prioridade", 90),
                           ("situacao", "Situação", 100)]:
    tabela.heading(c, text=titulo)
    tabela.column(c, width=largura)
tabela.pack(padx=10, pady=10, fill="both", expand=True)

lbl_contagem = tk.Label(janela, text="", font=("Arial", 11, "bold"))
lbl_contagem.pack(pady=5)

atualizar()
janela.mainloop()