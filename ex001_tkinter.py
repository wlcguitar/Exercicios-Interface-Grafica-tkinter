import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

def download_clicked():
    showinfo(
        title="Informação",
        message="Botão de download clicado!"
    )

root = tkinter.Tk()
root.title("Minha Aplicação Gráfica Tkinter GUI")
root.geometry("700x500")

bnt_icon = tkinter.PhotoImage(file="image\download.png")
lbl_image = tkinter.PhotoImage(file="image\Python.png")

tkinter.Label(
    root,
    image=lbl_image,
    compound="left"
).pack()

btn1 = ttk.Button(
    root,
    text="Sair",
    cursor="hand2",
    command=lambda: root.quit(),
)
btn1.pack()

btn2 = ttk.Button(
    root,
    text="Desabilitar",
    cursor="hand2",
    command=lambda: btn1.state(["disabled"])
)
btn2.pack()

btn3 =ttk.Button(
    root,
    text="Habilitar",
    cursor="hand2",
    command=lambda: btn1.state(["!disabled"])
)
btn3.pack()

btn4 = ttk.Button(
    root,
    text="",
    cursor="hand2",
    command=download_clicked,
    image=bnt_icon
)
btn4.pack()

root.mainloop()
