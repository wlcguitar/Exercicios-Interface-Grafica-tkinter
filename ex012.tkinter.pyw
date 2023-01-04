from tkinter import Tk, ttk
from tkinter.messagebox import showinfo
from random import randint

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Exibir barra de tarefas")
        self.resizable(False, False)
        self.geometry("300x150+500+150")
        self.paddings = {"padx":"10", "pady":"12"}
        self.tarefas = randint(2, 20)
        print(self.tarefas)

        #Progressbar
        self.progress_bar = ttk.Progressbar(self, mode="determinate", orient="horizontal", length=280)
        self.progress_bar.grid(row=0, column=0, columnspan=2, **self.paddings)

        #Value Label
        self.value_label = ttk.Label(self, text=self.update_value_label())
        self.value_label.grid(row=1, column=0, columnspan=2, **self.paddings)

        #Start Button
        self.start_button = ttk.Button(self, text="Iniciar", command=self.start_tasks)
        self.start_button.grid(row=2, column=0, **self.paddings)

        #Stop button
        self.stop_button = ttk.Button(self, text="Parar")
        self.stop_button.grid(row=2, column=1, **self.paddings)

    def update_value_label(self):
        return f"Progresso atual: {self.progress_bar['value']:.1f}%"

    def start_tasks(self):
        if self.progress_bar["value"] < 100:
            self.progress_bar["value"] += (100 / self.tarefas)
            self.value_label["text"] = self.update_value_label()

            self.after(randint(100,3000))

            self.id = self.after_idle(self.start_tasks)
            print(self.id)
        else:
            showinfo(title="Progresso tarefas", message="Tarefas concluidas com sucesso.")

    def stop(self):
        self.progress_bar.stop()
        self.value_label["text"] = self.update_value_label()
        self.after_cancel(self.id)


if __name__=="__main__":
    app = App()
    app.mainloop()
