from api_airfranceklm.utils import Location
from typing import Dict
import datetime


class Connection:
    """
    Représentation d'un itinéraire
    """
    def __init__(self,
                 departure_date: datetime.date,
                 departure_location: Location,
                 arrival_location: Location):
        """
        :param departure_date: Date de départ
        :param departure_location: Localisation de départ
        :param arrival_location: Localisation d'arrivée
        """
        self.departure_date = departure_date
        self.departure_location = departure_location
        self.arrival_location = arrival_location

    def to_dict(self) -> Dict:
        return {
            'departureDate': self.departure_date.isoformat(),
            'origin': self.departure_location.to_dict(),
            'destination': self.arrival_location.to_dict()
        }

