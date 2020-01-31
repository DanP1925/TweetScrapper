from enum import Enum
from datetime import timedelta

from twitterscraper import query_tweets

from day_tweets import DayTweets
from extended_file import ExtendedFile
from extended_tweet import ExtendedTweet


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

    def obtain_tweets_for(self, single_date):
        self.obtain_tweets_from(self.value["full_name"], single_date)
        self.obtain_tweets_from(self.value["abbreviation"], single_date)
        self.obtain_tweets_from("#" + self.value["abbreviation"], single_date)
        self.obtain_tweets_from(self.value["twitter_account"], single_date)

    def obtain_tweets_from(self, query_text, single_date):
        file = ExtendedFile(query_text, single_date)
        if file.has_tweets() and len(query_text) > 1:
            raw_tweets = query_tweets(
                query_text,
                begindate=single_date, enddate=single_date + timedelta(days=1),
                lang="es"
            )
            day_tweets = DayTweets(self, list(map(lambda raw_tweet: ExtendedTweet(raw_tweet.text), raw_tweets)))
            file = open(file.file_name, "w")
            day_tweets.write_on_file(file)
            file.close()

    def is_text_from(self, query_text):
        return query_text in [self.value["full_name"], self.value["abbreviation"], "#" + self.value["abbreviation"],
                              self.value["twitter_account"]]

    @staticmethod
    def get_from(file_name):
        query_text = file_name[:-15]
        if Party.CS.is_text_from(query_text):
            return Party.CS
        elif Party.IU.is_text_from(query_text):
            return Party.IU
        elif Party.PP.is_text_from(query_text):
            return Party.PP
        elif Party.PSOE.is_text_from(query_text):
            return Party.PSOE
        elif Party.PO.is_text_from(query_text):
            return Party.PO
        elif Party.UPYD.is_text_from(query_text):
            return Party.UPYD
        else:
            return None
