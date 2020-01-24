from datetime import timedelta, date
from os import path, stat

from twitterscraper import query_tweets

from extended_tweet import ExtendedTweet
from day_tweets import DayTweets
from party import Party


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def tomorrow(current_date):
    return current_date + timedelta(days=1)


def exist(file_name):
    return path.exists(file_name)


def is_empty(file_name):
    return stat(file_name).st_size == 0


def has_tweets(file_name):
    return (not exist(file_name)) or (exist(file_name) and is_empty(file_name))


def main():
    CAMPAIGN_END_DATE = date(2015, 9, 8)
    CAMPAIGN_START_DATE = date(2015, 9, 1)
    for party in Party.list():
        for single_date in daterange(CAMPAIGN_START_DATE, CAMPAIGN_END_DATE):
            file_name = "./output/" + party + "_" + single_date.strftime('%Y_%m_%d') + ".txt"
            if has_tweets(file_name):
                file = open(file_name, "w")
                day_tweets = DayTweets(query_tweets(party, begindate=single_date, enddate=tomorrow(single_date)))
                day_tweets.write_on_file(file)
                file.close()


if __name__ == "__main__":
    main()
