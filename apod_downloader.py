import requests
import json
import argparse
import os
import sys
import datetime
import config
from pathlib import Path
from tqdm import tqdm

def definePath(arguments):
	if arguments.path:
		if not arguments.path.endswith(os.path.sep):
			return arguments.path + os.path.sep + "Apod/"
		else:
			return arguments.path + "Apod/"
	else:
		return os.getcwd() + os.path.sep + "Apod/"

def defineHd(arguments):
	return "hdurl" if arguments.hd else "url"

def downloadImage(imageUrl, imagePath):
	try:
		response = requests.get(imageUrl, stream=True)
		response.raise_for_status()

		with open(imagePath, "wb") as file:
			with tqdm(
				total = int(response.headers.get("content-length", 0)),
				unit = "B",
				unit_scale=True,
				desc = "Téléchargement de " + imagePath.split('/')[-1],
			) as progressBar:
				for chunk in response.iter_content(chunk_size=8192):
					if chunk:
						file.write(chunk)
						progressBar.update(len(chunk))
	except requests.exceptions.RequestException as exception:
		print("Erreur de téléchargement : " + exception)

def Main():
	parser = argparse.ArgumentParser(description="Téléchargement des images de la NASA")
	parser.add_argument("--path", type=str, help="Chemin de destination des images")
	parser.add_argument("--delta", type=int, help="Delta par rapport à la date actuelle")
	parser.add_argument("--hd", type=int, help="Active le téléchargement des images en Haut Définition")
	arguments = parser.parse_args()

	DELTA_MAX = 365

	pathStorage = definePath(arguments)
	delta = arguments.delta or 0
	downloadType = defineHd(arguments)

	if delta > DELTA_MAX:
		print("Le delta doit être inférieur à " + DELTA_MAX)
		sys.exit(1)

	dateRecup = datetime.date.today() - datetime.timedelta(days=delta)
	print("=== Téléchargement à partir du " + str(dateRecup.strftime("%d/%m/%Y")) + " ===")

	url = "https://api.nasa.gov/planetary/apod?start_date=" + str(dateRecup) + "&api_key=" + config.NASA_API_KEY
	response = requests.get(url)
	
	try:
		data = json.loads(response.content)

		if "code" in data:
			print("Erreur API NASA: " + data['msg'])
			sys.exit(1)
		
		definitionMode = "Haute" if arguments.hd else "Base"
		print("=== Le téléchargement des images a été défini sur " + definitionMode + " Définition ===")
		print("=== Téléchargement des images dans '" + pathStorage + "' ===")

		nbDownloadImages = 0

		for item in data:
			Path(pathStorage).mkdir(parents=True, exist_ok=True)
			if item['media_type'] == "image":
				imageUrl = item[downloadType]
				imagePath = pathStorage + imageUrl.split("/")[-1]
				if not os.path.exists(imagePath):
					nbDownloadImages += 1
					downloadImage(imageUrl, imagePath)

		print("=== " + str(nbDownloadImages) + " image(s) téléchargée(s) ===")
	except json.decoder.JSONDecodeError as exception:
		print("Erreur de décodage des données JSON : " + str(exception))

if __name__ == "__main__":
	Main()
