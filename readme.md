# Weather app 

## __Description de l'application__ 
Architecture Python facilitant l'obtention d'informations relatives aux données météorologiques.<br>
Par la spécification d'une ville indiquée par l'utilisateur, l'application fait appel à l'API weatherapi.<br>
## __Architecture__ 

### `dossier View` : <br>
__view :__  gére l'affichage des différentes valeurs de l'application.

### `dossier controller` : <br>
__controller :__  classe qui permet de faire le lien entre le modele et la vue (maj de la vue ainsi que les demande utilisateurs)

### `dossier modèle` : <br>

__.ENV :__  le fichier qui contient la clé api (isolé) <br>
__API_meteo :__  contient la méthode qui permet d'appeler l'api au format JSON <br>
__Weather :__  contient toutes les méthodes appelant l'api <br>
__Fichier contenant "types" :__ contient les datatypes et les contraintes associés.


## __Librarie requises__  

- `Tkinter` 
- `python-dotenv`  
- `requests` 
- `os`
- `io`
- `urllib3`
- `Pillow`

## __lancement de l'application__ 

Pour fonctionner, il est nécessaire de posséder les différentes libraries requises. <br>
Par la suite il suffira d'exécuter le fichier `main.py`.