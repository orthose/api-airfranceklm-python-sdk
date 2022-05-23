from enum import Enum


class PassengerType(Enum):
    """
    Type de passager par classe d'âge
    """
    ADT = 1   # Adulte de plus de 16 ans
    CHD = 2   # Enfant entre 2 et 11 ans
    INF = 3   # Enfant de moins de 2 ans
    C14 = 4   # Jeune adulte entre 12 et 15 ans (UK)
    YTH = 5   # Jeune entre 12 et 18 ans
    YCD = 6   # Senior de plus de 65 ans
    STU = 7
    B12 = 8   # Jeune adulte de 12 ans (UK)
    B13 = 9   # Jeune adulte de 13 ans (UK)
    B14 = 10  # Jeune adulte de 14 ans (UK)
    B15 = 11  # Jeune adulte de 15 ans (UK)
    UNN = 12
    