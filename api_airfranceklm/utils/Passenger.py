from api_airfranceklm.utils import PassengerType
from typing import Optional, Dict
import datetime


class Passenger:
    """
    Représentation d'un passager
    """
    def __init__(self,
                 id: int,
                 type: PassengerType,
                 birth_date: Optional[datetime.date] = None):
        """
        :param id: Identifiant entre 0 et 99
        :param type: Type de passager en fonction de sa classe d'âge
        :param birth_date: Date de naissance
        """
        assert 0 <= id <= 99
        self.id = id
        self.type = type
        self.birth_date = birth_date

    def to_dict(self) -> Dict:
        res = {
            'id': self.id,
            'type': self.type.name
        }
        if self.birth_date is not None:
            res['birthDate'] = self.birth_date.isoformat()
        return res
