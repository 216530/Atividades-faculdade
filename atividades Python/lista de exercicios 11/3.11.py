import tkinter as tk
from tkinter import ttk, messagebox

cardapio = {
    "Hambúrguer": 25.00,
    "X-Salada": 28.00,
    "Batata frita": 15.00,
    "Refrigerante": 8.00,
    "Suco": 10.00
}

pedido = []

def moeda(valor):
    return f"R$ {valor:.2f}".replace(".", ",")

def atualizar_pedido():
    for item in tabela.get_children():
        tabela.delete(item)
    total = 0
    for p in pedido:
        subtotal = p["preco"] * p["quantidade"]
        total += subtotal
        tabela.insert("", "end", values=(p["produto"], p["quantidade"], moeda(p["preco"]), moeda(subtotal)))
    lbl_total.config(text=f"Total: {moeda(total)}")

def adicionar():
    produto = combo_produto.get()
    if not produto:
        messagebox.showwarning("Aviso", "Selecione um produto.")
        return

    try:
        quantidade = int(spin_quantidade.get())
        if quantidade <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Informe uma quantidade inteira maior que zero.")
        return

    for p in pedido:
        if p["produto"] == produto:
            p["quantidade"] += quantidade
            break
    else:
        pedido.append({"produto": produto, "preco": cardapio[produto], "quantidade": quantidade})

    spin_quantidade.delete(0, tk.END)
    spin_quantidade.insert(0, "1")
    atualizar_pedido()

def remover():
    selecionado = tabela.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um item para remover.")
        return
    indice = tabela.index(selecionado[0])
    pedido.pop(indice)
    atualizar_pedido()

def finalizar():
    if not pedido:
        messagebox.showwarning("Aviso", "O pedido está vazio.")
        return
    total = sum(p["preco"] * p["quantidade"] for p in pedido)
    messagebox.showinfo("Pedido finalizado", f"Pedido finalizado com sucesso!\nTotal a pagar: {moeda(total)}")
    pedido.clear()
    atualizar_pedido()

janela = tk.Tk()
janela.title("Lancheria")
janela.geometry("560x470")

frame_topo = tk.Frame(janela)
frame_topo.pack(pady=12)

tk.Label(frame_topo, text="Produto:").grid(row=0, column=0, padx=5)
combo_produto = ttk.Combobox(frame_topo, values=[f"{n}" for n in cardapio], state="readonly", width=18)
combo_produto.grid(row=0, column=1, padx=5)

tk.Label(frame_topo, text="Quantidade:").grid(row=0, column=2, padx=5)
spin_quantidade = tk.Spinbox(frame_topo, from_=1, to=99, width=5)
spin_quantidade.grid(row=0, column=3, padx=5)

tk.Button(frame_topo, text="Adicionar", command=adicionar).grid(row=0, column=4, padx=8)

frame_cardapio = tk.LabelFrame(janela, text="Cardápio")
frame_cardapio.pack(padx=10, pady=5, fill="x")
tk.Label(frame_cardapio,
         text="   |   ".join(f"{n}: {moeda(v)}" for n, v in cardapio.items()),
         font=("Arial", 8)).pack(pady=3)

colunas = ("produto", "quantidade", "preco", "subtotal")
tabela = ttk.Treeview(janela, columns=colunas, show="headings", height=10)
for c, titulo, largura in [("produto", "Produto", 180), ("quantidade", "Qtd", 60),
                           ("preco", "Preço unit.", 110), ("subtotal", "Subtotal", 110)]:
    tabela.heading(c, text=titulo)
    tabela.column(c, width=largura)
tabela.pack(padx=10, pady=10, fill="both", expand=True)

lbl_total = tk.Label(janela, text="Total: R$ 0,00", font=("Arial", 14, "bold"))
lbl_total.pack(pady=5)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=8)
tk.Button(frame_botoes, text="Remover item", width=14, command=remover).grid(row=0, column=0, padx=6)
tk.Button(frame_botoes, text="Finalizar pedido", width=14, command=finalizar).grid(row=0, column=1, padx=6)

janela.mainloop()