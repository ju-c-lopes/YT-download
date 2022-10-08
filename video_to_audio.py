# Python code to convert video to audio
import moviepy.editor as mp
import os

pasta = './'
files = []
for diretorio, subpastas, arquivos in os.walk(pasta):
#    print(diretorio)
#    if subpastas == "./.git":
#        print("ok")
    if diretorio.split("/")[1] == ".git":
        pass
    else:
        c = 1
        for arquivo in arquivos:
#            files.append([])
            print(f"{c} => {os.path.join(diretorio, arquivo)}")
            files.append(os.path.join(diretorio, arquivo))
#            files[c - 1].append(c)
            c += 1
        print("\nChoose the file number to convert: ", end=" ")

#print("\n")
#for n in files:
#    print(n)

your_choice = int(input())
your_file = files[your_choice - 1]


f = your_file.split(".")[-2]
f = f[1:]


# Insert Local Video File Path
clip = mp.VideoFileClip(r"{}".format(your_file))

#print(clip.audio)
# Insert Local Audio File Path
clip.audio.write_audiofile(r"{}.mp3".format(f))
