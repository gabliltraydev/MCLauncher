import tempfile
import os
import subprocess
import ctypes
import sys
from tkinter import filedialog
import tkinter
import uuid
from wget import *
from zipfile import *

tmpfolder = tempfile.gettempdir()


def baseFolder():
    if os.path.exists(tmpfolder + "/mcfolder.txt"):
        with open(tmpfolder + "/mcfolder.txt", 'r') as f:
            print(f.read())
    else:
        tkinter.messagebox.showinfo(title="Sélectionner un dossier",
                                    message="Merci de choisir le dossier d'installation des fichiers de votre launcher.")
        filename = filedialog.askdirectory()
        print("doss: " + filename)

        flpth = filename + "e.txt"
        try:
            filehandle = open(flpth, 'w')
        except IOError:
            tkinter.messagebox.showerror(title="Erreur",
                                         message="Dossier protégé par des autorisations administrateurs, merci de relancer le programme et de changer de dossier.")

            sys.exit("protected")

        with open(tmpfolder + "/mcfolder.txt", 'w') as f:
            f.write(filename)


def checkFolderExists():
    while os.path.getsize(tmpfolder + "/mcfolder.txt") == 0:
        tkinter.messagebox.showerror(title="Erreur",
                                     message="Vous n'avez pas indiqué de chemin, merci d'indiquer un chemin d'installation")

        filename = filedialog.askdirectory()
        print("doss: " + filename)

        flpth = filename + "e.txt"
        try:
            filehandle = open(flpth, 'w')
        except IOError:

            ctypes.windll.user32.MessageBoxW(0,
                                             "Dossier protégé par des autorisations administrateurs, merci de relancer le programme et de changer de dossier.",
                                             "Erreur", 0x10)
            sys.exit("protected")

        with open(tmpfolder + "/mcfolder.txt", 'w') as f:
            f.write(filename)


def downloadExtractFiles():
    with open(tmpfolder + "/mcfolder.txt", 'r') as f:
        folder = f.read()

    if os.path.exists(folder + "/jeu.bat") & os.path.exists(folder + "/runtime") \
            & os.path.exists(folder + "/versions") \
            & os.path.exists(folder + "/assets") \
            & os.path.exists(folder + "/libraries"):
        print("deja là")
    else:
        ctypes.windll.user32.MessageBoxW(0,
                                         "Lorsque vous cliquerez sur Ok, le téléchargement va commencer",
                                         "Téléchargement", 0)

        filepath = folder + "/game.zip"
        url = "http://gamezipfile.duckdns.org/game.zip"
        download(url, folder)

        zip = ZipFile(filepath)
        zip.extractall(folder)


def launchVerOne():
    downloadExtractFiles()
    with open(tmpfolder + "/mcfolder.txt", 'r') as f:
        folder = f.read()
    playerUUID = uuid.uuid1()
    uuidstr = str(playerUUID)
    print(uuidstr)

    psd = pseudo.get()

    with open(folder + "/nick.txt", 'w') as f:
        f.write(psd)
    with open(folder + "/uuid.txt", 'w') as f:
        f.write(uuidstr)

    subprocess.call(folder + "/jeu.bat")


baseFolder()
checkFolderExists()

root = tkinter.Tk()
root.geometry("900x600")
root.title("Launcher")

bgimg = tkinter.PhotoImage(file="bg.png")
btnBg = tkinter.PhotoImage(file="playbytton.png")
pseudo = tkinter.PhotoImage(file="playbytton.png")

limg = tkinter.Label(root, i=bgimg)
pseudo = tkinter.Entry(root, width=33)
start = tkinter.Button(root, height='80px', width='109px', command=lambda: launchVerOne(), borderwidth=0, image = btnBg)

pseudo.place(x=245, y=291, in_=root)
start.place(x=555, y=250, in_=root)
limg.pack()

root.mainloop()
