from os import getcwd
from posixpath import abspath
from tkinter import *
from tkinter import ttk
#import subprocess as sp
import youtube_dl as y



def mainWindow():

    def sd():
        yconf = {
            'outtmpl': 'c:\\output\\%(title)s.%(ext)s'
        }
        d = y.YoutubeDL(yconf)
        d.download([VIDEO_URL.get()])

    def hd():
        yconf = {
            'format': 'best',
            'outtmpl': 'c:\\output\\%(title)s.%(ext)s'
        }
        d = y.YoutubeDL(yconf)
        d.download([VIDEO_URL.get()])

    def mp3():
        yconf = {
            'format': 'bestaudio/best',
            'outtmpl': 'c:\\output\\%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }]
        }
        d = y.YoutubeDL(yconf)
        d.download([VIDEO_URL.get()])


    tdown = Tk()
    tdown.title("tdown downloader")
    tdown.resizable(0,0)

    f = Frame(tdown)
    f.pack(side=TOP)
    
    Label(f, text="Inserta la URL:").pack()
    VIDEO_URL = StringVar()
    url = Entry(f, textvariable=VIDEO_URL)
    url.pack()
    url.config(width=60)
    fd = Frame(tdown)
    fd.pack(side=TOP, fill=X, expand=True)
    Button(fd,text="SD", command=sd, background="yellow").pack(side=LEFT, fill=X, expand=True, pady=5, padx=2)
    Button(fd,text="HD", command=hd, background="yellow").pack(side=LEFT, fill=X, expand=True, pady=5, padx=2)
    Button(fd,text="MP3", command=mp3, background="yellow").pack(side=LEFT, fill=X, expand=True, pady=5, padx=2)
    

    
    

    tdown.mainloop()

if __name__=="__main__":
    mainWindow()