## DEPLOIEMENT D'UNE API PYTHON AVEC FASTAPI VIA DOCKER 

### Pour compiler la stack (d'1 seul service :/) avec docker compose
Sur un shell depuis la racine,
> docker-compose up
> ...

> ou pour avoir la reponse (au format json plus loin): après lancement du conteneur, curl http://127.0.0.1:8000/home (correspond à la sous rubrique définie dans le main)

### Pour apporter des modifs à l'appli python en backend
Activer l'environnement virtuel de préférence avant d'installer d'autres packages 
Sur un SHELL, depuis la racine :  
    -> python3 -m venv dockerize_fastapi
    -> dockerize_fastapi/Scripts/activate.bat

- installer les packages via pip dans une console Python
    -> exple : pip install fastapi uvicorn
    -> pour le test  en local, lancer fastapi avec la commande : uvicorn main:app --reload --port=8000

- après manips, ne pas oublier de : pip freeze > requirements.txt
