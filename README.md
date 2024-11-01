# YouTube Video Downloader

Este projeto é um aplicativo simples para baixar vídeos do YouTube com uma interface gráfica. Utilizando a biblioteca `yt_dlp`, permite que os usuários insiram uma URL de vídeo, selecionem um diretório de download e baixem o vídeo diretamente para o computador, com uma barra de progresso indicando o andamento do download.

## Download

Você pode baixar o executável do projeto clicando [aqui](https://github.com/user-attachments/files/17535180/VideoDownloader.zip).

## Funcionalidades

- **Download de vídeos** do YouTube com escolha de diretório.
- **Interface gráfica** amigável com barra de progresso para acompanhar o download.
- **Botão para abrir o diretório** do vídeo após o download ser concluído.

## Pré-requisitos

- Python 3.x
- Bibliotecas necessárias:
  - `yt_dlp`: Biblioteca para download de vídeos do YouTube e outras plataformas de vídeo.
  - `tkinter`: Biblioteca padrão do Python para criação de interfaces gráficas.
- **FFmpeg**: Para mesclar vídeo e áudio (requerido apenas em downloads que utilizam formatos separados).

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/KemuellKlinger/VideoDownloader.git
   ```

2. Instale o `yt_dlp`, se ainda não estiver instalado:
   ```bash
   pip install yt-dlp
   ```

3. **Instale o FFmpeg**:
   - **Linux**: Use o comando `sudo apt install ffmpeg` (ou o correspondente para sua distribuição).
   - **Windows**: Siga as instruções de instalação [aqui](https://ffmpeg.org/download.html).

## Estrutura do Projeto

```
nome-do-repositorio/
├── AppJanela/
│   ├── Barra.py         # Classe Barra, responsável pela barra de progresso.
│   ├── Buttones.py      # Classe Buttones, responsável pelos botões.
│   ├── Janela.py        # Classe Janela, responsável pela janela principal do app.
├── main.py              # Arquivo principal para iniciar o aplicativo.
└── README.md            # Explicação do projeto.
```

## Como Usar

1. No terminal, execute o script principal:
   ```bash
   python main.py
   ```

2. No aplicativo:
   - Cole a URL do vídeo do YouTube que deseja baixar.
   - Selecione o diretório de destino para salvar o vídeo.
   - Clique em "Baixar" para iniciar o download.
   - Uma barra de progresso irá exibir o andamento do download.
   - Após a conclusão, o botão "Abrir Diretório" aparecerá. Clique nele para abrir a pasta onde o vídeo foi salvo.

## Observações

- **Compatibilidade com SO**: Para Windows, ajuste a linha de código `subprocess.Popen(['xdg-open', directory])` no método `open_directory` para `subprocess.Popen(f'explorer "{directory}"')`.
- **Segurança**: Este projeto utiliza bibliotecas externas para baixar vídeos; certifique-se de respeitar as políticas de uso de cada plataforma.

## Dependências

- `yt_dlp`: Para baixar vídeos de sites de hospedagem de vídeos.
- `tkinter`: Para a interface gráfica.
- `FFmpeg`: Para mesclar áudio e vídeo, caso necessário.
