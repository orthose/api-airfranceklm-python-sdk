# Introduction
SDK Python pour requêter l'API REST de Airfrance KLM. Développé dans le cadre du projet de chatbot Marley 
pour permettre aux utilisateurs d'obtenir des recommandations de billets d'avion.

* **Auteur** : Maxime Vincent
* **Unité Enseignement** : Projet Apprentissage
* **Enseignant** : M. Sylvain Conchon
* **Formation** : Master M1 ISD
* **Établissement** : Université Paris-Saclay

# Documentation
Pour se connecter à l'API il faut créer un compte via le nouveau [portail](https://developer.airfranceklm.com/). 
La documentation de l'API est plus complète sur l'ancien [portail](https://docs.airfranceklm.com/) mais pas forcément
à jour. Il faut la croiser avec la nouvelle [documentation](https://developer.airfranceklm.com/resources).

Pour le moment ce SDK est très limité et ne permet d'effectuer que quelques requêtes de la section
[Offers](https://developer.airfranceklm.com/documentations/api/A000021/versions/1.0.0/pages/documentation) de la base OpenData.

# Utilisation
Ce SDK peut être construit sous forme d'une archive wheel pour être installé dans un environnement Python.
```commandline
./build.sh
pip install dist/api_airfranceklm-0.0.0-py2.py3-none-any.whl
```

Ou de manière plus simple à l'aide du lien du dépôt github.
```commandline
pip install git+https://github.com/orthose/api-airfranceklm-python-sdk.git
```

Il est ensuite possible d'utiliser l'API en l'important au début d'un script Python.
```python
from api_airfranceklm.open_data import offers
```
Pour avoir des exemples d'utilisation vous pouvez consulter les fichiers `tests/test*`.

# Architecture
Le module `open_data.offers` met à disposition plusieurs fonctions indépendantes qui sont des requêtes HTTPS à l'API.
Pour paramétrer ces fonctions il faut utiliser les constructeurs du module `utils`.
J'ai fait ce choix d'architecture afin de robustifier le paramétrage avec notamment des types énumérés.
