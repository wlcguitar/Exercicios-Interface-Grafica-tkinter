#3º Exercicio tkinter
import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tkinter.Tk()
root.title("Widget Entry")
root.geometry("600x400")
root.attributes("-topmost", 1)

def btn_clicked(event=None):
    if texto.get() != "Insira seu nome...":
        msg = "Seja bem vindo(a) {}!".format(texto.get())
        showinfo(title="Informação", message=msg)
        texto.set("Insira seu nome...")
        text_box.select_range(0 ,tkinter.END)
        text_box.focus()

       
texto = tkinter.StringVar()
texto.set("Insira seu nome...")

text_box = ttk.Entry(
    root,
    textvariable=texto,
    font="Arial 11"
)
text_box.select_range(0 ,tkinter.END)
text_box.focus()
text_box.bind("<Return>", btn_clicked)
text_box.pack()


btn = ttk.Button(
    root,
    text="Executar",
    command=btn_clicked
)
btn.pack()

root.mainloop()
