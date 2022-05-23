from api_airfranceklm.utils import LocationType
from typing import Dict


class Location:
    """
    Représentation d'une localisation
    """
    def __init__(self, type: LocationType, code: str):
        """
        :param type: Type de localisation (aéroport ou ville)
        :param code: Code IATA (https://fr.wikipedia.org/wiki/Liste_des_codes_IATA_des_a%C3%A9roports/A)
        """
        self.type = type
        self.code = code

    def to_dict(self) -> Dict:
        code_dict = {'code': self.code}
        if self.type.name == 'AIRPORT':
            return {'airport': code_dict}
        elif self.type.name == 'CITY':
            return {'city': code_dict}
