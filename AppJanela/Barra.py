from tkinter import * 
from tkinter import ttk
import time

class Barra:
    def __init__(self, master):
        self.varBarra = DoubleVar()
        self.varBarra.set(0)
        self.progresso = ttk.Progressbar(master, variable=self.varBarra, maximum=100)
        self.progresso.pack(pady=10)

    def atualizarBarra(self, progresso):
        self.varBarra.set(progresso)