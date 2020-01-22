from datetime import timedelta, date

from twitterscraper import query_tweets

from party import Party


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def tomorrow(current_date):
    return current_date + timedelta(days=1)


def main():
    CAMPAIGN_END_DATE = date(2015, 9, 8)
    CAMPAIGN_START_DATE = date(2015, 9, 1)
    base_name = "output"
    for party in Party.list():
        for single_date in daterange(CAMPAIGN_START_DATE, CAMPAIGN_END_DATE):
            file = open(base_name + "_" + party + "_" + single_date.strftime('%Y_%m_%d') + ".txt", "w")
            list_of_tweets = query_tweets(party, begindate=single_date, enddate=tomorrow(single_date))
            for tweet in list_of_tweets:
                file.write(str(tweet.text))
            file.close()


if __name__ == "__main__":
    main()
