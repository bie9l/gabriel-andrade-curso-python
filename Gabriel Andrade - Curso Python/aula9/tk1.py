from tkinter import *

janela = Tk()

label = Label(janela, text="Bielzin", font=('Arial', 12))
label.pack()


frame = Frame(janela, width=200, height=200, relief=RAISED, bd=50, bg='blue' )
frame.pack()


# canvas = Canvas(janela, width=600, height=500)
# canvas.pack()

# canvas.create_rectangle(100, 100, 1000, 600, fill='blue')

check_var = BooleanVar()

check_button = Checkbutton(janela, text= 'Aceitar os termos!', 
variable=check_var.get())
check_button.pack()

radio_var = StringVar()

radio1 = Radiobutton(janela, text='Opção 1', variable=radio_var,
value='opcao1', state='normal' )#opcoes= normal, disabled, active
radio2 = Radiobutton(janela, text='Opção 1', variable=radio_var,
value='opcao2', state='normal' )
radio1.pack()
radio2.pack()

scale_var = DoubleVar()
scale = Scale(janela, width=200, from_=100, to=0)
scale.pack()



def click_button():
    label.config(text='Cruzeiro')
    print(check_var.get())


# text = StringVar()

# input = Entry(janela, textvariable=text, bg='blue')
# input.pack()

# text_box = Text(janela, height=50, width=70 )

# text_box.pack()

# text_box.insert(END, 'Esse é um exemplo de caixa de texto')

# def click_button():
#     label.config(text=text.get())


button = Button(janela, width=100, text='Clique em mim', command=click_button)
button.pack()



janela.mainloop()
