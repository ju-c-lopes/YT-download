import colorama
from colorama import Fore, Style
from pytube import YouTube
import os
import time
colorama.init

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

link = input("Enter the link: ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)








def list_options():
    print("\nType which of them you want to download:\n")
    for i in range(len(yt.streams)):
        print(f"{i + 1} => {yt.streams[i].mime_type}   -   {yt.streams[i].abr if yt.streams[i].abr else yt.streams[i].resolution}")
        time.sleep(0.3)

    your_choice = int(input("\nNumber: "))
    return your_choice



cancel = 0
while True:

    try:
        if cancel > 2:
            cancel_confirm = input("Deseja cancelar? Y/N ")
            cancel_confirm = cancel_confirm.lower()

            while cancel_confirm != "y" and cancel_confirm != "n":
                cancel_confirm = input("Deseja cancelar? Y/N ")
                cancel_confirm = cancel_confirm.lower()
            if cancel_confirm == "y":
                print("Cancelado com sucesso\n")
                break
        y_c = list_options()
        if y_c > 0:
            ys = yt.streams[y_c - 1]

            #Starting download
            print(Fore.RED + "\nDownloading...")
        ys.download()
        print(Fore.GREEN + "Download completed!!\n")
        break
    except:
        print("Your choice doesn't exists")
    cancel += 1


