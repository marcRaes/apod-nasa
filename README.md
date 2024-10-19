# apod-nasa

## Script de téléchargement d'images APOD de la NASA

Ce script Python permet de télécharger les images de l'Astronomy Picture of the Day (APOD) de la NASA. Il offre la possibilité de spécifier un chemin de destination, un delta de jours à remonter et de choisir entre une résolution haute définition ou standard.

### Installation

1.  **Assurez-vous d'avoir Python 3** installé sur votre système.

2.  **Installez les bibliothèques requises** à l'aide de pip :

	```
	pip install requests json argparse os sys datetime pathlib tqdm
	```

**Options:**

-  `--path`: Spécifie le chemin où vous souhaitez enregistrer les images. Par défaut, les images sont enregistrées dans un sous-dossier "Apod" du répertoire courant.
-  `--delta`: Télécharge les images à partir d'une date décalée de `delta` jours par rapport à la date actuelle (maximum 365 jours).
-  `--hd`: Télécharge les images en haute définition (HD) (par défaut : définition standard).

**Exemples:**

- Télécharger l'image APOD la plus récente dans le répertoire courant :

	```
	python apod_downloader.py
	```
- Télécharger les images APOD des trois derniers jours dans un dossier personnalisé nommé "ImagesNASA" en haute définition :

	```
	python apod_downloader.py --path "ImagesNASA" --delta 3 --hd
	```

### Fonctionnalités

-  **Téléchargement flexible:** Choisissez la date de début et la résolution des images.
-  **Gestion d'erreurs:** Le script gère les erreurs potentielles comme les réponses API invalides ou les erreurs de décodage JSON.
-  **Barre de progression:** Une barre de progression indique l'avancement du téléchargement de chaque image.
-  **Création automatique de dossiers:** Le script crée automatiquement les dossiers nécessaires si ceux-ci n'existent pas.

### Avertissement

- Il vous faudra posséder une clé API NASA afin de faire fonctionner ce script. Vous pouvez obtenir une clé API sur [https://api.nasa.gov/](https://api.nasa.gov/)

- Dans le fichier config.py remplacer `{MA_CLE_API}` par votre propre clé API NASA.

### Licence

Ce script est fourni sans licence explicite. Vous êtes libre de l'utiliser, de le modifier et de le distribuer selon vos besoins.
