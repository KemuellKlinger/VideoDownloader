import yt_dlp
import re
import threading
import os
from AppJanela.Janela import *
from AppJanela.Barra import *
from tkinter import *
import subprocess

class VideoDownloader:
    def __init__(self, url, progress_bar, janela, on_complete):
        self.url = url
        self.progress_bar = progress_bar
        self.janela = janela
        self.on_complete = on_complete
        self.progress_label = None
        self.video_path = None
        self.ydl_opts = {
            'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            'outtmpl': f"{janela.caminho_entrada.get()}/%(title)s.%(ext)s",
            'progress_hooks': [self.progress_hook]
        }

    def limpar_ansi(self, texto):
        ansi_escape = re.compile(r'(?:\x1B[@-_][0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', texto)

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            progresso_str = self.limpar_ansi(d['_percent_str']).replace('%', '').strip()
            progresso = float(progresso_str)
            self.progress_bar.atualizarBarra(progresso)

            progresso_texto = f"Baixando... {progresso:.2f}%"
            if self.progress_label:
                self.progress_label.config(text=progresso_texto)
            else:
                self.progress_label = Label(self.janela.root, text=progresso_texto, bg=self.janela.corFundo)
                self.progress_label.pack()

        elif d['status'] == 'finished':
            self.video_path = d['filename']
            self.janela.msgAviso("Download concluído com sucesso!")
            self.on_complete()  # Chama a função de callback após o download

    def download(self):
        try:
            self.janela.addTexto("Iniciando o download...")
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([self.url])
        except Exception as e:
            self.janela.msgErro(f"Ocorreu um erro: {e}")

class App:
    def __init__(self):
        self.janela = Janela("Download YT", 350, 400, "gray")
        self.entrada = self.janela.addEntrada('Cole a URL aqui', 30, 10)
        self.janela.addGetCaminho("Selecione o caminho", 30, 10)
        
        # Botão inicialmente invisível
        self.btAbrir = Buttones()
        self.btAbrir.addBotao("Abrir Diretório", self.open_directory)
        self.btAbrir.bb.pack_forget()  # Esconde o botão inicialmente

        self.btBaixar = Buttones()
        self.btBaixar.addBotao("Baixar", self.start_download)

    def open_directory(self):
        if hasattr(self, 'downloader') and self.downloader.video_path:
            directory = os.path.dirname(self.downloader.video_path)
            subprocess.Popen(['xdg-open', directory])  # Para Linux
            # subprocess.Popen(f'explorer "{directory}"')  # Para Windows
        else:
            self.janela.msgErro("O caminho do vídeo não foi encontrado.")

    def start_download(self):
        url = self.entrada.get()
        if url:
            progress_bar = Barra(self.janela.root)
            self.downloader = VideoDownloader(url, progress_bar, self.janela, self.show_open_button)
            threading.Thread(target=self.downloader.download).start()
        else:
            self.janela.msgAviso("Digite algo no campo")

    def show_open_button(self):
        # Mostra o botão após o download
        self.btAbrir.bb.pack()  # Exibe o botão

if __name__ == "__main__":
    app = App()
    app.janela.root.mainloop()
