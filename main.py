from datetime import timedelta, date
from os import listdir

from day_tweets import DayTweets
from party import Party


def main():
    CAMPAIGN_END_DATE = date(2015, 10, 1)
    CAMPAIGN_START_DATE = date(2015, 9, 1)

    obtain_all_tweets(CAMPAIGN_START_DATE, CAMPAIGN_END_DATE)
    create_summary()


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
            continue
        file = open("./output/" + file_name, "r")
        days_tweets.append(DayTweets.read_from_file(Party.get_from(file_name), file))
        file.close()

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


if __name__ == "__main__":
    main()
