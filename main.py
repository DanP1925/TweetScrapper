from datetime import timedelta, date

from twitterscraper import query_tweets

from ExtendedTweet import ExtendedTweet
from party import Party


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def tomorrow(current_date):
    return current_date + timedelta(days=1)


def main():
    CAMPAIGN_END_DATE = date(2015, 9, 7)
    CAMPAIGN_START_DATE = date(2015, 9, 1)
    for party in Party.list():
        if party != Party.PO.value and party != Party.UPD.value:
            continue
        for single_date in daterange(CAMPAIGN_START_DATE, CAMPAIGN_END_DATE):
            file = open("./output/" + party + "_" + single_date.strftime('%Y_%m_%d') + ".txt", "w")
            raw_tweets = query_tweets(party, begindate=single_date, enddate=tomorrow(single_date))
            tweets = list(map(lambda raw_tweet: ExtendedTweet(raw_tweet), raw_tweets))
            file.write("Total Tweets: " + str(len(raw_tweets)) + '\n')
            total_words = 0
            total_tokens = []
            for tweet in tweets:
                for sentence in tweet.sentences:
                    total_words += len(sentence.words)
                    total_tokens += sentence.tokens
            total_tokens = list(dict.fromkeys(total_tokens))
            file.write("Total Words: " + str(total_words) + '\n')
            file.write("Total Tokens: " + str(len(total_tokens)) + '\n')
            tweet_index = 1
            for tweet in tweets:
                file.write(str(tweet_index) + "." + '\n')
                file.write(tweet.raw_tweet + '\n')
                file.write("--------------------------------------" + '\n')
                tweet_index += 1
            file.close()


if __name__ == "__main__":
    main()
