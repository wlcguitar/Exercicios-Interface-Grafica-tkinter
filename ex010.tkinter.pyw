import tkinter
from tkinter.messagebox import showinfo

main_window = tkinter.Tk()
main_window.title("Tkinter GUI")
main_window.geometry("280x100+250+150")
main_window.resizable(False, False)
main_window.attributes("-topmost", 1)


def welcome(event=False):
    if txt.get() != "Insira seu nome...":
        msg = f"Seja bem vindo(a) {txt.get()}!!!"
        showinfo(title="Informação", message=msg)
        txt.set("Insira seu nome...")
        text_box.select_range(0, tkinter.END)
        text_box.focus()


txt = tkinter.StringVar()
txt.set("Insira seu nome...")

text_box = tkinter.Entry(
    main_window,
    font="Time 12",
    textvariable=txt
)
text_box.bind("<Return>", welcome)
text_box.focus()
text_box.select_range(0, tkinter.END)
text_box.pack(ipadx=35, ipady=2)

btn = tkinter.Button(
    main_window,
    text="Executar",
    command= welcome
)
btn.pack()


main_window.mainloop()
