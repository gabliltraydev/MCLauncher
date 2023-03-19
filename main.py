import subprocess
import ctypes
from tkinter import filedialog, messagebox
import tkinter
import uuid
from wget import *
from zipfile import *

TEMP_FOLDER = tempfile.gettempdir()
INSTALLATION_FOLDER = os.path.join(TEMP_FOLDER, "mcfolder.txt")
DOWNLOAD_URL = "download_url"


def create_base_folder():
    while not os.path.exists(INSTALLATION_FOLDER):
        messagebox.showinfo(title="Sélectionner un dossier",
                            message="Merci de choisir le dossier d'installation des fichiers de votre launcher.")
        file_name = filedialog.askdirectory()
        check_admin_file = file_name + "_check_admin.txt"
        print(file_name)
        try:
            filehandle = open(check_admin_file, 'w')
        except IOError:
            tkinter.messagebox.showerror(title="Erreur",
                                         message="Dossier protégé par des autorisations administrateurs, merci de "
                                                 "relancer le programme et de changer de dossier.")

            sys.exit("protected")

        with open(TEMP_FOLDER + "/mcfolder.txt", 'w') as f:
            f.write(file_name)

    while os.path.getsize(TEMP_FOLDER + "/mcfolder.txt") == 0:
        messagebox.showerror(title="Erreur",
                             message="Vous n'avez pas indiqué de chemin, merci d'indiquer un chemin d'installation")

        filename = filedialog.askdirectory()
        print("doss: " + filename)

        file_path = filename + "_check_admin.txt"
        try:
            filehandle = open(file_path, 'w')
        except IOError:
            messagebox.showerror(title="Erreur",
                                 message="Dossier protégé par des autorisations administrateurs, merci de relancer le "
                                         "programme et de changer de dossier.")
            sys.exit("protected")

        with open(TEMP_FOLDER + "/mcfolder.txt", 'w') as f:
            f.write(filename)


def download_extract_files():
    with open(TEMP_FOLDER + "/mcfolder.txt", 'r') as f:
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

        file_path = folder + "/game.zip"

        download(DOWNLOAD_URL, folder)

        zip_file_mc1_12_2 = ZipFile(file_path)
        zip_file_mc1_12_2.extractall(folder)


def launch_ver_one():
    download_extract_files()
    with open(TEMP_FOLDER + "/mcfolder.txt", 'r') as f:
        folder = f.read()
    player_uuid = uuid.uuid1()
    uuid_string = str(player_uuid)
    print(uuid_string)

    player_pseudo = pseudo_field.get()

    with open(folder + "/nick.txt", 'w') as f:
        f.write(player_pseudo)
    with open(folder + "/uuid.txt", 'w') as f:
        f.write(uuid_string)

    subprocess.call(folder + "/jeu.bat")


create_base_folder()

root = tkinter.Tk()
root.geometry("900x600")
root.title("Launcher")
root.resizable(False, False)

background_image = tkinter.PhotoImage(file="bg.png")
button_background = tkinter.PhotoImage(file="playbytton.png")

window_background = tkinter.Label(root, i=background_image)
pseudo_field = tkinter.Entry(root, width=33)
start_button = tkinter.Button(root, height='80px', width='109px', command=lambda: launch_ver_one(), borderwidth=0,
                              image=button_background)

pseudo_field.place(x=245, y=291, in_=root)
start_button.place(x=555, y=250, in_=root)
window_background.pack()

root.mainloop()
