import tkinter as tk
from tkinter import ttk

def mudar_cor(arg):
    root.config(background=arg)
    print("Botão pressionado!!!")


def return_press(event):
    print("Tecla enter pressionada!!!")


def log(event):
    print(event)


root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+300+250")
root.resizable(False, False)
root.attributes("-alpha", 0.90)
root.attributes("-topmost", 1)
root.iconbitmap("Aula159\python.ico")
root.state("normal")

lbl = ttk.Label(
    root,
    text="Mudar Cor",
    font="Arial 12",
)
lbl.pack()

btn1 = ttk.Button(
    root,
    text="Cinza",
    padding=8,
    command=lambda: mudar_cor("grey")
)
btn1.bind("<Return>", return_press)
btn1.bind("<Return>", log, add="+")
btn1.pack()

btn2 = ttk.Button(
    root,
    text="Azul",
    padding=8,
    command=lambda: mudar_cor("Blue")
)
btn2.bind("<Return>", return_press)
btn2.pack()

btn3 = ttk.Button(
    root,
    text="Vermelho",
    padding=8,
    command=lambda: mudar_cor("Red")
)
btn3.bind("<Return>", return_press)
btn3.pack()

root.mainloop()
