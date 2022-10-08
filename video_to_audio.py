# Python code to convert video to audio
import moviepy.editor as mp
import os

pasta = './'
files = []
for diretorio, subpastas, arquivos in os.walk(pasta):



    if diretorio.split("/")[1] == ".git":
        pass
    else:
        c = 1
        for arquivo in arquivos:

            print(f"{c} => {os.path.join(diretorio, arquivo)}")
            files.append(os.path.join(diretorio, arquivo))

            c += 1
        print("\nChoose the file number to convert: ", end=" ")





your_choice = int(input())
your_file = files[your_choice - 1]


f = your_file.split(".")[-2]
f = f[1:]


# Insert Local Video File Path
clip = mp.VideoFileClip(r"{}".format(your_file))


# Insert Local Audio File Path
clip.audio.write_audiofile(r"{}.mp3".format(f))
