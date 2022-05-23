import re
from typing import Optional, Dict


class Context:
    """
    Définition du contexte des requêtes à l'API Airfrance KLM
    Permet d'initialiser les headers principaux utilisés par chaque requête
    """

    def __init__(self,
                 api_key: Optional[str] = None,
                 api_key_file: Optional[str] = None,
                 content_type: Optional[str] = "application/json",
                 accept: Optional[str] = "application/hal+json;charset=utf8",
                 accept_language: Optional[str] = "fr-FR",
                 afkl_travel_host: Optional[str] = "AF"):
        """
        Initialisation des headers principaux
        :param api_key: Clé de l'API
        :param api_key_file: Chemin du fichier contenant la clé de l'API
        :param content_type: Type de contenu envoyé
        :param accept: Type de message attendu en réponse
        :param accept_language: Langage accepté {{language}}-{{country}}
        :param afkl_travel_host: AF ou KL
        """
        assert (api_key is None) ^ (api_key_file is None)
        if api_key_file is not None:
            with open(api_key_file, 'r') as f:
                api_key = f.read()
        assert re.match(r'^[a-zA-Z0-9]{24}$', api_key)
        assert re.match(r'^[a-z]+-[A-Z]+$', accept_language) is not None
        assert afkl_travel_host in ('AF', 'KL')
        self.api_key = api_key
        self.content_type = content_type
        self.accept = accept
        self.accept_language = accept_language
        self.afkl_travel_host = afkl_travel_host

    def get_headers(self) -> Dict:
        """
        Obtenir les headers principaux nécessaires à la connexion
        :return: Dictionnaire des headers modifiable et extensible
        """
        return {
            'Api-Key': self.api_key,
            'Content-Type': self.content_type,
            'Accept': self.accept,
            'Accept-Language': self.accept_language,
            'AFKL-TRAVEL-Host': self.afkl_travel_host
        }
