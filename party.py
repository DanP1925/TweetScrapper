from enum import Enum


class ExtendedEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class Party(ExtendedEnum):
    CS = "Ciudadanos"
    IU = "Izquierda Unida"
    PP = "Partido Popular"
    PSOE = "Partido Socialista Obrero Espanol"
    PO = "Podemos"
    UPD = "Union Progreso y Democracia"
