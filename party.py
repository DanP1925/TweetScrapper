from enum import Enum


class Party(Enum):
    CS = {
        "full_name": "Ciudadanos",
        "abbreviation": "C's",
        "twitter_account": "@CiudadanosCs"
    }
    IU = {
        "full_name": "Izquierda Unida",
        "abbreviation": "IU",
        "twitter_account": "@iunida"
    }
    PP = {
        "full_name": "Partido Popular",
        "abbreviation": "PP",
        "twitter_account": "@populares"
    }
    PSOE = {
        "full_name": "Partido Socialista Obrero Español",
        "abbreviation": "PSOE",
        "twitter_account": "@PSOE"
    }
    PO = {
        "full_name": "Podemos",
        "abbreviation": "",
        "twitter_account": "@Podemos_Unidos"
    }
    UPYD = {
        "full_name": "Unión Progreso y Democracia",
        "abbreviation": "UPyD",
        "twitter_account": "@UPYD"
    }

    def get_full_name(self):
        return self.value["full_name"]

    def get_abbreviation(self):
        return self.value["abbreviation"]

    def get_hashtag(self):
        return "#" + self.value["abbreviation"]

    def get_twitter_account(self):
        return self.value["twitter_account"]
