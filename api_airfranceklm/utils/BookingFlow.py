from enum import Enum


class BookingFlow(Enum):
    """
    Type de réservation
    """
    REWARD = 1  # Récompense
    CORPORATE = 2  # Entreprise
    LEISURE = 3  # Loisir
    STAFF = 4  # Personnel naviguant
    