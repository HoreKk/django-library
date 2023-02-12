## Django Library Project

Une simple application de gestion de bibliothèque.
Il est possible de créer des livres, des auteurs, des genres, des éditeurs et des groupes de lectures.
Il existe 3 types de comptes : les clients, les libraires et les administrateurs.

# Setup

### Synchroniser la base de données
```
python3 manage.py migrate --run-syncdb
```

#### Populer la base de donnée
```
python3 manage.py loaddata library/fixtures/dump.json
```

#### Lancer le serveur
```
python3 manage.py runserver
```

#### Lancer le serveur de développement de Tailwind (uniquement en mode développement)
```
python3 manage.py tailwind start
```



# Projet 

### Client 

Nom d'utilisateur: **client**, Mot de passe: **passwordclient**

### Libraire

Nom d'utilisateur: **librarian**, Mot de passe: **passwordlibrarian**

### Administrateur (sur l'interface d'administration '/admin')

Nom d'utilisateur: **admin**, Mot de passe: **password**

### Fonctionnalités

Le client peut :

- Consulter la liste des livres et par recherche
- Participer à des session d'un groupe de lecture donné

Le libraire peut :

- Ajouter, modifier et supprimer des livres (ainsi que les auteurs, genres, collections et éditeurs)
- Ajouter des groupes de lecture et des sessions de lecture
- Accepter ou refuser les demandes de participation aux sessions de lecture