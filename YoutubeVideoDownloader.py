from tkinter import *
from tkinter import ttk

from pytube import YouTube
from tkinter import filedialog

Folder_Name = "C:\ Users\dsr07\Downloads"
def OpenLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name, fg="green")
    else:
        locationError.config(text="Invalid Location", fg="red")

def getDetails() : 
    pass

def DownloadVideo():
    global Folder_Name
    url = ytdEntry.get()
    if(len(url) > 1):
        ytdError.config(text="")
        video = YouTube(url)
        video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(Folder_Name)
        ytdError.config(text="Video Downloaded Successfully", fg="green", font=("jost", 12))

root = Tk()
root.title("Video Downloader")
root.geometry("360x360")

root.columnconfigure(0, weight=1)

ytdLabel = Label(root, text="Enter video URL",font=("jost",15))
ytdLabel.grid()

ytdEntryvar = StringVar()
ytdEntry = Entry(root, width="50", textvariable=ytdEntryvar)
ytdEntry.focus()
ytdEntry.grid()

ytdError = Label(root, text="", fg="red", font=("jost", 12))
ytdError.grid()

saveEntry = Button(root, width=30, bg="red", fg="white", text="choose file location", command=OpenLocation)
saveEntry.grid()

locationError = Label(root, text="C:\ Users\dsr07\Downloads", fg="green", font=("jost", 12))
locationError.grid()

download = Button(root, text="Download", width=10, bg="red", fg="white", command=DownloadVideo)
download.grid()

root.mainloop()