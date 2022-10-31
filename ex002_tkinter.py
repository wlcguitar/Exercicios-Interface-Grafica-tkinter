import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title("Entry Widget")
root.geometry("400x100")

#Armazenar os valores do text box
texto = tkinter.StringVar()
texto.set("Insira seu nome..")

text_box = tkinter.Entry(
    root,
    textvariable=texto,
    font="Arial 12",
    cursor="hand2"
)
text_box.select_range(0, tkinter.END)
text_box.focus()
text_box.pack()

btn = ttk.Button(
    root,
    text="Executar",
    command=lambda: print(text_box.get()),
    cursor="hand2"
)
btn.pack()

root.mainloop()
