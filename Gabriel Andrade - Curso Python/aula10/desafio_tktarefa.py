# Desafio: Criar uma lista de tarefas
# - Deve ser possível adicionar uma tarefa
# - Deve ser possível remover uma tarefa
# - Tarefas: Nome, descrição e prioridade (Combobox)
# - Devem ser exibidas numa Treeview.


from distutils.dir_util import remove_tree
from tkinter import *
from tkinter.ttk import *

from click import ClickException
from pyautogui import click



janela = Tk()


tree_view = Treeview(janela)
tree_view['columns'] = ('nome_tarefa', 'prioridade', 'descricao',)

tree_view.column('#0', width=100, minwidth=100, anchor='center')
tree_view.column('nome_tarefa', width=150, minwidth=150, anchor='center')
tree_view.column('prioridade', width=150, minwidth=150, anchor='center')
tree_view.column('descricao', width=150, minwidth=150, anchor='center')

tree_view.heading('#0', text='ID')
tree_view.heading('nome_tarefa', text='TAREFA')
tree_view.heading('prioridade', text='PRIORIDADE')
tree_view.heading('descricao', text='DESCRICAO')

tree_view.pack()

label_name = Label(janela, text="Digite o nome da tarefa.")
label_name.pack()
entry_name = Entry(janela, text='Digite o nome da tarefa')
entry_name.pack()


label_prioridade = Label(janela, text="Digite a prioridade da tarefa.")
label_prioridade.pack()
entry_prioridade = Entry(janela, text='Digite a prioridade da tarefa')
entry_prioridade.pack()


label_descricao = Label(janela, text="Digite a descrição da tarefa.")
label_descricao.pack()
entry_descricao = Entry(janela, text='Digite a descrição da tarefa')
entry_descricao.pack()


i = 0


def add_tarefa():
    name = entry_name.get()
    prioridade = entry_prioridade.get()
    descricao = entry_descricao.get()
    id = len(tree_view.get_children())
    item = tree_view.insert('', END, text=id+1, values=(name, prioridade, descricao))
    print(name)
    print(prioridade)
    print(descricao)
    tree_view.pack()


button_add = Button(janela, width=100, text='Adicionar tarefa', command=add_tarefa)
button_add.pack()

def remove_tarefa():
    remove_tree()


button_remove = Button(janela, width=100, text='Remover tarefa', command=remove_tarefa)
button_remove.pack()


janela.mainloop()