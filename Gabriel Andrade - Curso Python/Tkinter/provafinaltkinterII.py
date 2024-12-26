import tkinter as tk

def validador():
    email = entry_text.get()
    senha = entry_text2.get()
    if "@" in email and len(senha) > 6:
        label_resultado.config(text="Login realizado com sucesso!")
    else:
        label_resultado.config(text="Por favor, insira um login válido seguindo as restrições.")

root = tk.Tk()
root.title("Tela de login!")
root.geometry("800x600")


label = tk.Label(root, text="Bem-vindo a tela de login!", font=("Arial", 16))
label_instrucao = tk.Label(root, text="Faça seu login com seu email e com sua senha com mais de 6 digitos: ", font=("Arial", 16))
label.pack()
label_instrucao.pack()

label_email = tk.Label(root, text="Email:", font=("Arial", 13))
label_email.pack()
entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text)
entry.pack()

label_senha = tk.Label(root, text="Senha:", font=("Arial", 13))
label_senha.pack()
entry_text2 = tk.StringVar()
entry2 = tk.Entry(root, textvariable=entry_text2)
entry2.pack()

button = tk.Button(root, text="Fazer login", command=validador)
button.pack()


label_resultado = tk.Label(root, text="", font=("Arial", 16))
label_resultado.pack(pady=10)

root.mainloop()