from enum import Enum


class PromoType(Enum):
    """
    Type de promotion
    """
    LOWEST_FARE = 1
    PROMO_FARE = 2
    LOWEST_PROMO_FARE = 3
    