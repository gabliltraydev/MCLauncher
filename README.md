# McLauncher
Launcher Minecraft OpenSource développé par moi en Python

Executable minecraft fait par https://github.com/rxmii6z
----------------------------------------------------------
Allez lire le ReadMe de [ce repo](https://github.com/gabliltraydev/Minecraft-Portable/) afin de prendre la version de minecraft qui vous intéresse (vous pouvez également créer votre version custom avec des mods préinstallés ou encore une version non disponible)

## Si vous avez trouvé une version toute faite 
- Téléchargez les fichiers du launcher
(le code en python est bon pour lancer une seule version, si vous voulez juste lancer une version de MC en particulier ne touchez pas au code autre que la ligne que vous allez devoir changer après)
- Modifiez la variable "DOWNLOAD_URL" dans le fichier "main.py" en remplaçant "download_url" par celle de votre fichiez ZIP à télécharger avec le lien copié à l'aide du tuto dans le readme de [ce repo](https://github.com/gabliltraydev/Minecraft-Portable/)
-  Modifier dans le code la ligne "file_path = folder + "/game.zip" en remplaçent "game.zip" par la version choisie (par exemple, si vous avez pris la 1.8.9 Vanilla, le lien est "https://github.com/gabliltraydev/Minecraft-Portable/releases/download/Releases/Vanilla.1.8.9.zip" et donc le .zip s'appelle "Vanilla.1.8.9.zip", donc vous devrez modiier "game.zip" par "Vanilla.1.8.9.zip"
- ⚠️ Ne pas modifier le nom des dossiers et du .bat éxécutable, sinon le launcher ne fonctionnera pas ⚠️

## Si vous avez vous-même fait votre version grace à [ce repo]((https://github.com/gabliltraydev/Minecraft-Portable/blob/main/Version%20de%20Base/readme.md)
- Allez dans le dossier ou se trouve les fichiers puis sélectionez tout et faites Clic-Droit --> Envoyer-vers --> Dossier Compressé
- Nommez le dossier compressé "game.zip"
- Uploadez le sur une plateforme de stockage de fichiers ou vous pouvrez avoir un lien de téléchargement direct (google drive par exemple ou github)
- Modifiez la variable "DOWNLOAD_URL" dans le fichier "main.py" en remplaçant "download_url" par celle de votre fichiez ZIP à télécharger

Et voilà, votre launcher est fonctionnel et télécharge la version que vous avez choisi :)

Amusez vous bien !
