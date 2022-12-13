import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tkinter.Tk()
root.title("Progressbar Tkinter.")

def label_progresso():
    return f"Progresso atual: {barra_progresso['value']}%"


def progresso():
    if barra_progresso["value"] < 100:
        barra_progresso["value"] += 20
        valor_label["text"]=label_progresso()
    else:
        showinfo(title="Informação", message="O progresso está completo!")


def stop():
    barra_progresso.stop()
    valor_label['text']=label_progresso()


label_frame = ttk.Labelframe(
    root,
    text="Barra de Progresso",
)
label_frame.pack(ipadx=10, ipady=10, fill="both", expand=True)

barra_progresso = ttk.Progressbar(
    label_frame,
    orient="horizontal",
    length=300
)
barra_progresso.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

valor_label = ttk.Label(
    label_frame,
    text=label_progresso()
)
valor_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

btn_start = ttk.Button(
    label_frame,
    text="Start",
    command=progresso
)
btn_start.grid(row=2, column=0, padx=5, pady=5)

btn_stop = ttk.Button(
    label_frame,
    text="Stop",
    command=stop
)
btn_stop.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
