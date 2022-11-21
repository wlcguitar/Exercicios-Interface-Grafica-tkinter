from tkinter import Button, Tk, ttk

def log(event=None):
    print("Testando evento...")


root = Tk()
root.title("Minha Aplicação Tkinter GUI")
root.geometry("600x400+250+150")


btn1 = ttk.Button(
    root,
    text=("Executar"),
    command=log
)
btn1.bind("<Return>", log)
btn1.focus()
btn1.pack()

btn2 = ttk.Button(
    root,
    text="Desvincular Evento",
    command=lambda: btn1.unbind("<Return>")
)
btn2.pack()

root.mainloop()
