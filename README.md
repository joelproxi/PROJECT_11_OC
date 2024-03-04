# Project_LitReviews
Projet réalisé dans le cadre de ma formation OpenClassrooms Développeur d'Applications Python.  
Il s'agit d'une application web réalisée avec flask pour une société fictive, GÜDLFT.  
L'application est un site permettant de reserver des places de compétitions pour des clubs.

## Fonctionnalités

* Inscription / connexion.
* Consulter son solde de places.
* Reserver des places dans une compétition.


## Installation & lancement

Commencez tout d'abord par installer Python.  
Lancez ensuite la console, placez vous dans le dossier de votre choix :
 - cd"Nom_du_dossier"

 Puis clonez ce repository dans le dossier de votre choix:
- git clone https://github.com/Evan-Snd/PROJECT_11_OC.git

Placez vous dans le dossier P9_sinda_evan :
 - cd P9_sinda_evan

Puis créez un nouvel environnement virtuel si cela n'est pas déja fait:
 - python -m venv env

Ensuite, activez cet environnement
Windows:
 - env\scripts\activate.bat

Linux:
 - source env/bin/activate

Installez ensuite les packages requis:
 - pip install -r requirements.txt

Il ne vous reste plus qu'à lancer le serveur
Windows:
- $env:FLASK_APP = "server.py"
- flask run

Linux :
- export FLASK_APP=server.py
- flask run

Vous pouvez ensuite utiliser l'applicaton à l'adresse suivante:
 - http://127.0.0.1:5000

Il existe déja trois utilisateurs sur le site :
- john@simplylift.co
- admin@irontemple.com"
- kate@shelifts.co.uk"




