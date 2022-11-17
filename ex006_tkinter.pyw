import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        # label
        self.label = ttk.Label(self, text="Ola, Tkinter!")
        self.label.pack(**options)

        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack(**options)

        self.pack(**options)
    
    def button_clicked(self):
        showinfo(title="Informação", message="Ola Tkinter!!!")


class App(tk.Tk):
    def __init__(self):
        super().__init__()  
        self.title("Minha App Tkinter POO")
        self.geometry("300x100+750+350")

if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()