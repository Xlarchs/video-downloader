import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

root = tk.Tk()
root.geometry("550x110")
root.title("Youtube Video Downloader")
root.resizable(False, False)
root.config(background="gray")

def Ayarlar():
    linkYeri = Label(root, text="Video linki giriniz : ", bg="gray")
    linkYeri.grid(row=1, column=0, pady=5, padx=5)

    root.linkYaz = Entry(root, width=70)
    root.linkYaz.grid(row=1, column=1, pady=5, padx=5, columnspan = 2)

    hedefYeri = Label(root, text="Kayıt yeri : ", bg="gray")
    hedefYeri.grid(row=2, column=0, pady=5, padx=5)

    root.hedefYazi = Entry(root, width=40)
    root.hedefYazi.grid(row=2, column=1, pady=5, padx=5)

    kayitButonu = Button(root, text="Kayit", command=Kayit, width=20)
    kayitButonu.grid(row=2, column=2, pady=5, padx=5)

    indirmeButonu = Button(root, text="indir", command=indir, width=40)
    indirmeButonu.grid(row=3, column=1, pady=5, padx=5)

def Kayit():

    root.hedefDIR= filedialog.askdirectory(initialdir="C:\Python")
    root.hedefYazi.insert('1', root.hedefDIR)

def indir():
 
    getVideo = YouTube(root.linkYaz.get())
    videoStream = getVideo.streams.first()
    videoStream.download(root.hedefDIR)
    messagebox.showinfo("BAŞARILI", "VİDEO İNDİRİLİP KAYDEDİLDİ\n"+root.hedefDIR)







Ayarlar()


root.mainloop()

    
