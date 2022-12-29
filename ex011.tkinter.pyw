import tkinter
from tkinter import ttk

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Temas Tkinter")
        self.style = ttk.Style()

        padding = {"padx":5, "pady":5, "stick": "we"}

        #Widget Label 
        self.label_titutlo = ttk.Label(self, text="Nome:")
        self.label_titutlo.grid(row=0, column=0, **padding)

        #Widget Entry
        self.widget_entry = ttk.Entry(self)
        self.widget_entry.grid(row=0, column=1, **padding)

        #widget button
        self.button_executar = ttk.Button(self, text="Executar")
        self.button_executar.grid(row=0, column=2, **padding)

        #widget radiobutton
        self.selecionar_temas = tkinter.StringVar()
        self.widget_labelframe = ttk.Labelframe(self, text="Temas")
        self.widget_labelframe.grid(row=1, columnspan=3, ipadx=10, ipady=10, **padding)

        for tema in self.style.theme_names():
            ttk.Radiobutton(
                self.widget_labelframe,
                variable=self.selecionar_temas,
                text=tema,
                value=tema,
                command=self.mudar_tema
            ).pack(expand=True, padx=5, pady=5, fill='x')


    def mudar_tema(self):
        self.style.theme_use(self.selecionar_temas.get())


if __name__=="__main__":
    app = App()
    app.mainloop()
