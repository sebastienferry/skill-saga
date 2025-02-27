# API Projet

Ce projet est une API en Python pour gérer une liste triée d'objectifs ou de jalons. L'API permet de regrouper les éléments en différents paliers et de leur attribuer des étiquettes.

## Structure du projet

```
api-projet
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   └── __init__.py
│   ├── routes
│   │   └── __init__.py
│   ├── services
│   │   └── __init__.py
│   └── utils
│       └── __init__.py
├── requirements.txt
└── README.md
```

## Installation

1. Clonez le dépôt :
   ```
   git clone <url-du-depot>
   cd api-projet
   ```

2. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancez l'application :
   ```
   python app/main.py
   ```

2. Accédez à l'API via `http://localhost:5000` (ou le port configuré).

## Endpoints

- `GET /objectifs` : Récupère la liste des objectifs.
- `POST /objectifs` : Crée un nouvel objectif.
- `PUT /objectifs/{id}` : Met à jour un objectif existant.
- `DELETE /objectifs/{id}` : Supprime un objectif.

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre une demande de tirage pour toute amélioration ou correction.

## License

Ce projet est sous licence MIT.