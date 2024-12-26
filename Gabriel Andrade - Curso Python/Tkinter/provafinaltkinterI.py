import tkinter as tk


def conversor():
    cm = entry_text.get()
    try:
        cm = float(cm)
        metros = cm / 100
        label_resultado.config(text=f"{cm} cm equivalem a {metros:.2f} metros.")
    except ValueError:
        label_resultado.config(text="Por favor, insira um número válido.")


root = tk.Tk()
root.title("Conversor centimetros para metros!")
root.geometry("800x600")



label = tk.Label(root, text="Bem-vindo ao conversor!", font=("Arial", 16))
label_instrucao = tk.Label(root, text="Digite quantos centimetros você quer converter para metros: ", font=("Arial", 16))
label.pack()
label_instrucao.pack()


entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text)
entry.pack()


button = tk.Button(root, text="Converter", command=conversor)
button.pack()


label_resultado = tk.Label(root, text="", font=("Arial", 16))
label_resultado.pack(pady=10)

root.mainloop()