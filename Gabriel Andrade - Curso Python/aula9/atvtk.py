# pedir nome, idade, nota, exibir botao para fazer append dos dados em um dicionario e printar no final

from tkinter import *

janela = Tk()

label = Label(janela, text="Bem-vindo ao cadastramento!", font=('Arial', 12))
label.pack()

nome = StringVar()
idade = StringVar()
nota = StringVar()
lista_aluno = []



label = Label(janela, height=5, width=50, text="Digite o nome do aluno.", font=('Arial', 12))
label.pack()
# text_box1 = Text(janela, height=5, width=50 )
# text_box1.pack()
# text_box1.insert(END, 'Digite o nome do aluno.')
input_nome = Entry(janela, textvariable=nome, bg='white')
input_nome.pack()

label = Label(janela, height=5, width=50, text="Digite a idade do aluno.", font=('Arial', 12))
label.pack()
# text_box2 = Text(janela, height=5, width=50 )
# text_box2.pack()
# text_box2.insert(END, 'Digite a idade do aluno.')
input_idade = Entry(janela, textvariable=idade, bg='white')
input_idade.pack()

label = Label(janela, height=5, width=50, text="Digite a nota do aluno.", font=('Arial', 12))
label.pack()
# text_box3 = Text(janela, height=5, width=50 )
# text_box3.pack()
# text_box3.insert(END, 'Digite a nota do aluno.')
input_nota = Entry(janela, textvariable=nota, bg='white')
input_nota.pack()


def click_button():
    label.config(text='Enviado!')
    print("Os dados cadastrados foram: ")
    print(f'Nome do aluno: {nome.get()}')
    print(f'Idade do aluno: {idade.get()}')
    print(f'Nota do aluno: {nota.get()}')
    aluno = { 'Nome': nome.get(), 'Idade': idade.get(), 'Nota': nota.get()}
    lista_aluno.append(aluno)
    nome.set('')
    idade.set('')
    nota.set('')
    
def ver_notas():
    print(lista_aluno)

button = Button(janela, width=100, text='Enviar dados', command=click_button)
button.pack()

button2 = Button(janela, width=100, text='Ver dados', command=ver_notas)
button2.pack()

janela.mainloop()