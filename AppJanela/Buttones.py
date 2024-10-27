from tkinter import Button

class Buttones:
    def __init__(self):
        self.button_func = None  # Inicializa a função de callback

    def addBotao(self, info, func=None, espacamento=None):
        self.button_func = func
        self.bb = Button(text=info, command=self.clickBotao)
        self.bb.pack(pady=espacamento)
        return self.bb

    def clickBotao(self):
        if self.button_func:
            self.button_func()
