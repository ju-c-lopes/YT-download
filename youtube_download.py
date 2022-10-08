
from pytube import YouTube
import time

link = input("Enter the link: ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the highest resolution possible
#ys = yt.streams.get_highest_resolution()

# = 0
#for detail in yt.streams:
#    i += 1


print("\nType which of them you want to download:\n")
for i in range(len(yt.streams)):
    print(f"{i + 1} => {yt.streams[i].mime_type}   -   {yt.streams[i].abr if yt.streams[i].abr else yt.streams[i].resolution}")
    time.sleep(0.5)

your_choice = int(input("\nNumber: "))

try:
    if your_choice > 0:
        ys = yt.streams[your_choice - 1]


        #Starting download
        print("\nDownloading...")
    ys.download()
    print("Download completed!!\n")
except:
    print("Your choice doesn't exists")

