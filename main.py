from datetime import timedelta, date
from os import listdir

from day_tweets import DayTweets
from party import Party


def main():
    CAMPAIGN_END_DATE = date(2015, 9, 8)
    CAMPAIGN_START_DATE = date(2015, 9, 1)

    obtain_all_tweets(CAMPAIGN_START_DATE, CAMPAIGN_END_DATE)
    #create_summary()


def obtain_all_tweets(start_date, end_date):
    for party in Party:
        for single_date in date_range(start_date, end_date):
            party.obtain_tweets_for(single_date)


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


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


if __name__ == "__main__":
    main()
