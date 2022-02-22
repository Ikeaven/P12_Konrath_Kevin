# P12_Konrath_Kevin
Développez une architecture back-end sécurisée en utilisant Django ORM - Epic Events

## 1. Récupérer le projet :

    $ git clone https://github.com/Ikeaven/P12_Konrath_Kevin.git

Se déplacer dans le repertoire du projet :

    $ cd P12_Konrath_Kevin

## 2. Créer et activer un environnement virtuel :

    $ python3 -m venv env

    $ source env/bin/activate [Mac/linux]
    $ env\Scripts\activate.bat [Windows]

## 3. Installer les dépendances :

    $ pip install -r requirements.txt


## 4. Lancer le serveur Postgre SQL sur le port 5432, ou modifier les settings du projet Django

    Une base de donnée postgre SQL au nom de "epic_events_db" doit être créer dans postgres
    Le serveur postgres doit être lancé :
        https://www.postgresql.org/docs/

## 5. Créer un super utilisateur :

    $ cd CRM_Epic_Events
    $ ./manage.py createsuperuser

    Suivre les instructions de la console

## 6. Démarrer le serveur de développement :

    $ ./manage.py runserver
    L'API sera accessible à l'adresse locale 127.0.0.1:8000 par défaut
    Si le port n'est pas disponible :
    $ ./manage.py runserver <your_port>

## 7. Naviguer ves l'éspace d'administration :

    Ouvrir un navigateur à l'adresse :
    http://127.0.0.1:8000/admin/
    Rentrer les identifiants du superuser pour se connecter en tant qu'administrateur

## 8. Documentation de l'API :
https://documenter.getpostman.com/view/11117999/UVknsFra#bd91f23e-5eeb-4322-9375-571825acdc57
