from tkinter import *
from tkinter import messagebox, filedialog
from AppJanela.Buttones import Buttones

class Janela:
    def __init__(self, titulo, largura, altura, corPadrao=None):
        self.root = Tk()
        largura_screen = self.root.winfo_screenwidth()
        altura_screen = self.root.winfo_screenheight()
        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - (altura + 70) / 2
        self.root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        self.root.title(titulo)
        self.button_func = None
        self.var = StringVar()
        self.root.config(background=corPadrao)
        self.corFundo = corPadrao
        self.caminho_entrada = None

    def destruir(self):
        return self.root.destroy()
    
    def addTexto(self,info, x=None, y=None):
        self.label = Label(text=info, bg=self.corFundo)
        if x is not None and y is not None:
           self.label.place(x=x, y=y)
        else:
            self.label.pack()

    def addEntrada(self, tt=None, largura=None, espacamento=None, x=None, y=None):
        if tt:
            self.addTexto(tt)
        self.valorEntrada = Entry(width=largura)
        if x is not None and y is not None:
            self.valorEntrada.place(x=x, y=y)
        else:
            self.valorEntrada.pack(pady=espacamento)   
        return self.valorEntrada
    
    def msgAviso(self, msg):
        messagebox.showinfo("Aviso", msg)
    def msgAlerta(self, msg):
        messagebox.showwarning("Alerta", msg)
    def msgErro(self, msg):
        messagebox.showerror("Erro", msg)

    def addCheck(self, info):
        var = BooleanVar()
        checkbox1 = Checkbutton(self.root, text=info, variable=var, bg=self.corFundo)
        checkbox1.pack()
        return var
    
    def addSelecao(self, info, valor):
        radio_button = Radiobutton(self.root, text=info, variable=self.var, value=valor, bg=self.corFundo)
        radio_button.pack()
        return valor
    
    def addGetCaminho(self, titulo, largura=None, espacamento=None):
        # Adiciona um botão para selecionar o caminho
        btCaminho = Buttones()
        btCaminho.addBotao(titulo, lambda:self.selecionar_caminho(espacamento))

        # Campo de entrada para exibir o caminho
        self.caminho_entrada = Entry(self.root, width=largura)
        
    
    def selecionar_caminho(self, esp=None):
        # Abre o diálogo para selecionar o diretório
        caminho = filedialog.askdirectory()
        if caminho:  # Verifica se um caminho foi selecionado
            self.caminho_entrada.pack(pady=esp)
            self.caminho_entrada.delete(0, END)  # Limpa a entrada atual
            self.caminho_entrada.insert(0, caminho)  # Insere o novo caminho

