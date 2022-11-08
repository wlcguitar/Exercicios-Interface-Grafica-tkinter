import tkinter 
from tkinter import ttk
from tkinter.messagebox import showinfo

class JanelaPrincipal(tkinter.Tk):
    def __init__(self):
        super().__init__()
    #Configurar a janela.
        self.title("Minha Aplicação Tkinter POO")
        self.geometry("350x100")
        self.iconbitmap("Exercicios_tkinter\image\Documento.ico")
        self.attributes("-topmost", 1)
        self.resizable(False, False)
    #Configurar os widgets.
        self.lbl = ttk.Label(
            self,
            text="Janela ShowInfor"
            )
        self.lbl.pack()

        self.btn = ttk.Button(
            self, 
            text="Executar", 
            cursor="hand2", 
            command=self.informacao
            )
        self.btn.pack()

    def informacao(self):
        showinfo(title="Informação", message="Vou vencer, Em nome de Jesus!!!")

if __name__=="__main__":
    janela = JanelaPrincipal()
    janela.mainloop()
