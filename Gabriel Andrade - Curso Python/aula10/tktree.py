from tkinter import *
from tkinter.ttk import *

ten_emails = ['amanda@gmail.com', 'thiago@gmail.com', 'luis@gmail.com', 'victor@gmail.com', 'carla@gmail.com', 'raiane@gmail.com', 'camille@gmail.com', 'roberto@gmail.com', 'jose@gmail.com', 'felipe@gmail.com']

ten_names = ['Amanda', 'Thiago', 'Luis', 'Victor', 'Carla', 'Raiane', 'Camille', 'Roberto', 'José', 'Felipe']

# Criar um Tree View utilizando o TK inter, com duas colunas contendo as informações de nome e email cadastrados.

janela = Tk()




label_name = Label(janela, text="Digite seu nome.")
label_name.pack()
entry_name = Entry(janela, text='Digite seu nome')
entry_name.pack()

label_email = Label(janela, text="Digite seu email.")
label_email.pack()
entry_email = Entry(janela, text='Digite seu email')
entry_email.pack()


tree_view = Treeview(janela)
tree_view['columns'] = ('nome', 'email')

tree_view.column('#0', width=100, minwidth=100, anchor='center')
tree_view.column('nome', width=150, minwidth=150, anchor='center')
tree_view.column('email', width=150, minwidth=150, anchor='center')

tree_view.heading('#0', text='ID')
tree_view.heading('nome', text='NOME')
tree_view.heading('email', text='EMAIL')

# tree_view.insert('', END, text='1', values=('Walter', 'walter@email.com'))

i = 0

for name in ten_names:
    tree_view.insert('', END, text=str(i+1), values=(name, ten_emails[i]))
    i += 1


def add_people():
    name = entry_name.get()
    email = entry_email.get()
    id = len(tree_view.get_children())
    item = tree_view.insert('', END, text=id+1, values=(name, email))
    print(name)
    print(email)
    tree_view.pack()


button = Button(janela, width=100, text='Enviar dados', command=add_people)
button.pack()


tree_view.pack()
janela.mainloop()