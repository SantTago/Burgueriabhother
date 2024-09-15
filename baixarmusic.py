from pytube import YouTube
import os

def baixar_audio(youtube_url):
    # Cria a pasta "Musicas" se ela não existir
    if not os.path.exists('Musicas'):
        os.makedirs('Musicas')

    # Baixa o vídeo
    yt = YouTube(youtube_url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path='Musicas')

    # Renomeia o arquivo para mp3
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(f"Audio baixado e salvo como: {new_file}")

# Exemplo de uso
link = "https://www.youtube.com/watch?v=vN0dkdr-OT0"
baixar_audio(link)
