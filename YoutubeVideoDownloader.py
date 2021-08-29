from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

root = Tk()
root.title("Video Downloader")
root.geometry("360x400")

root.columnconfigure(0, weight=1)

ytdLabel = Label(root, text="Enter video URL",font=("jost",15))
ytdLabel.grid()

ytdEntryvar = StringVar()
ytdEntry = Entry(root, width="50", textvariable=ytdEntryvar)
ytdEntry.focus()
ytdEntry.grid()

ytdError = Label(root, text="Error Msg", fg="red", font=("jost", 12))
ytdError.grid()

saveLabel = Label(root, text="Save Video", font=("josh", 14, 'bold'))
saveLabel.grid()

saveEntry = Button(root, width=30, bg="red", fg="white", text="choose file location")
saveEntry.grid()

locationError = Label(root, text="Invalid Location", fg="red", font=("jost", 12))
locationError.grid()

qualityLabel = Label(root, text="Select Video quality", font=("jost", 12))
qualityLabel.grid()

choices = [720, 420, 360, 1080]
YtdChoices = ttk.Combobox(root, width=30, values=choices)
YtdChoices.grid()

download = Button(root, text="Download", width=10, bg="red", fg="white")
download.grid()

developerLabel = Label(root, text="Alkairis", font=("josh", 14, 'bold'))
developerLabel.grid()

root.mainloop()