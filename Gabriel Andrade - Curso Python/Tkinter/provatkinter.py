# import tkinter as tk



# def change_label_text():
#     label.config(text="Texto alterado!")



# root = tk.Tk()

# root.title("Janela de Exemplo")



# label = tk.Label(root, text="Olá!", font=("Arial", 16))

# label.pack()



# button = tk.Button(root, text="Alterar Texto", command=change_label_text)

# button.pack()


# root.mainloop()



# import tkinter as tk



# root = tk.Tk()

# root.title("Janela de Exemplo")

# root.geometry("400x300")



# label = tk.Label(root, text="Bem-vindo!", font=("Arial", 16))

# label.pack()



# button = tk.Button(root, text="Clique Aqui", padx=10, pady=5, bg="blue", fg="white")

# button.pack()


# root.mainloop()



import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Criando uma barra de progresso
progress = ttk.Progressbar(root, length=200, mode='determinate', maximum=100)
progress.pack()

# Atualizando o valor da barra de progresso
progress['value'] = 95  # Exemplo de como definir o progresso

root.mainloop()
