from datetime import timedelta, date
from os import path, stat, listdir

from twitterscraper import query_tweets

from extended_tweet import ExtendedTweet
from day_tweets import DayTweets
from party import Party


def main():
    CAMPAIGN_END_DATE = date(2015, 9, 8)
    CAMPAIGN_START_DATE = date(2015, 9, 1)

    obtain_all_tweets(CAMPAIGN_START_DATE, CAMPAIGN_END_DATE)
    create_summary()


def obtain_all_tweets(start_date, end_date):
    for party in Party:
        for single_date in daterange(start_date, end_date):
            obtain_tweets_from(party.get_full_name(), single_date)
            if len(party.get_abbreviation()) > 1:
                obtain_tweets_from(party.get_abbreviation(), single_date)
            if len(party.get_hashtag()) > 1:
                obtain_tweets_from(party.get_hashtag(), single_date)
            obtain_tweets_from(party.get_twitter_account(), single_date)


def obtain_tweets_from(query_text, single_date):
    file_name = "./output/" + query_text + "_" + single_date.strftime('%Y_%m_%d') + ".txt"
    if has_tweets(file_name):
        file = open(file_name, "w")
        raw_tweets = query_tweets(query_text, begindate=single_date, enddate=tomorrow(single_date), lang="es")
        day_tweets = DayTweets(list(map(lambda raw_tweet: ExtendedTweet(raw_tweet.text), raw_tweets)))
        day_tweets.write_on_file(file)
        file.close()


def create_summary():
    total_tweets = 0
    total_words = 0
    token_list = []
    file_names = listdir('output')
    days_tweets = []
    for file_name in file_names:
        if not file_name[-4:] == ".txt":
            break
        file = open("./output/" + file_name, "r")
        days_tweets.append(DayTweets.read_from_file(file))
        file.close()
    for day_tweets in days_tweets:
        total_tweets += day_tweets.total_tweets
        total_words += day_tweets.total_words
        token_list += day_tweets.tokens
    print(total_tweets)
    print(total_words)
    print(len(list(dict.fromkeys(token_list))))


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


if __name__ == "__main__":
    main()
