from enum import Enum


class FareOption(Enum):
    """
    Tarif optionnel
    """
    CORSICA = 1
    FAMILY = 2
    FLEXIBLE = 3
    UM_OPTIONAL = 4
    UM_MANDATORY = 5
