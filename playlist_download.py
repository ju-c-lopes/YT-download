import colorama
from colorama import Fore, Style
from pytube import Playlist
from time import sleep
import os
colorama.init(autoreset=True)

def check_packages():
    up = False

    # Verificará se o pacote pytube está atualizado
    tube_pkg = os.popen("pip list -o")
    pipe = tube_pkg.read()
    tube_pkg.close()
    
    if pipe.find("pytube") != -1:
        os.system("pip install --upgrade pytube")
        print("\nPacote PyTube atualizado.")
        up = True
    
    # Verificará se o pacote colorama está atualizado
    if pipe.find("colorama") != -1:
        os.system("pip install --upgrade colorama")
        print("\nPacote Colorama atualizado.")
        up = True
    
    if not up:
        print("\nSem atualizações de pacotes.")
    print()

check_packages()

link = input("Enter the playlist: ")
playlist = Playlist(link)

i = 0

def select_video(yt):

    for i in range(len(yt.streams)):
        print("yt streams abr: ", yt.streams[i + 1].abr)
        if yt.streams[i].abr[-4:] == "kbps" and yt.streams[i + 1].abr is None:
            print(f"Selecting video version: {yt.title} - {yt.streams[i].abr}")
            return i

for video in playlist.videos:

    try:
        indice = select_video(video)
        print(Fore.RED + "\nDownloading => " + Fore.BLUE + f"{video.title}")
        video.streams[indice].download()
    except:
        print("It was impossible to download this video")
        sleep(3)
        continue
    sleep(3)
    print(Fore.GREEN + "Download completed!!\n")
    print(str(i) + " ok")
    i += 1
