from enum import Enum


class MakeEnum(Enum):
    AUDI = "AUDI"
    BMW = "BMW"
    MB = "MERCEDES-BENZ"
    VW = "VOLKSWAGEN"


class FuelEnum(Enum):
    D = "Diesel"
    P = "Petrol"
    G = "LPG"


class ColorEnum(Enum):
    B = "Black"
    G = "Green"
    Y = "Yellow"
    W = "White"


class BodyTypeEnum(Enum):
    E = "Estate"
    H = "Hatchback"
    S = "Saloon"
