from abc import ABC, abstractmethod
from os import listdir

from day_tweets import DayTweets
from party import Party
from summary_detail import SummaryDetail
from utils import Utils


class SummaryGeneratorFactory:

    @staticmethod
    def create_summary_generator(summary_detail):
        if summary_detail == SummaryDetail.TWEET_NUMBERS:
            return TweetSummaryGenerator()
        elif summary_detail == SummaryDetail.FULL:
            return FullSummaryGenerator()


class SummaryGenerator(ABC):

    @abstractmethod
    def generate_summary(self):
        pass


class TweetSummaryGenerator(SummaryGenerator):

    def generate_summary(self):
        num_tweets = 0
        file_names = listdir('output')
        for file_name in file_names:
            if not Utils.is_text_file(file_name):
                continue
            with open("./output/" + file_name, "r", encoding="unicode_escape") as file:
                line = file.readline()
                if not line:
                    continue
                words = line.split()
                num_tweets += int(words[2])

        print("Total tweets: " + str(num_tweets))


class FullSummaryGenerator(SummaryGenerator):

    def generate_summary(self):
        total_tweets = 0
        total_words = 0
        token_list = []
        file_names = listdir('output')
        days_tweets = []
        for file_name in file_names:
            if not Utils.is_text_file(file_name):
                continue
            with open("./output/" + file_name, "r", encoding="utf-8") as file:
                days_tweets.append(DayTweets.read_from_file(Party.get_from(file_name), file))

        for day_tweets in days_tweets:
            total_tweets += day_tweets.total_tweets
            total_words += day_tweets.total_words
            token_list += day_tweets.tokens

        print("Resumen")
        print("Total tweets: " + str(total_tweets))
        print("Total words: " + str(total_words))
        print("Total tokens: " + str(len(list(dict.fromkeys(token_list)))))
        print()

        for party in Party:
            party_tweets = 0
            party_words = 0
            party_token_list = []
            for day_tweets in days_tweets:
                if day_tweets.party == party:
                    party_tweets += day_tweets.total_tweets
                    party_words += day_tweets.total_words
                    party_token_list += day_tweets.tokens
            print(party.get_full_name())
            print("Total tweets: " + str(party_tweets))
            print("Total words: " + str(party_words))
            print("Total tokens: " + str(len(list(dict.fromkeys(party_token_list)))))
            print()
