from extended_tweet import ExtendedTweet


class DayTweets:

    def __init__(self, raw_tweets):
        self.tweets = list(map(lambda raw_tweet: ExtendedTweet(raw_tweet), raw_tweets))
        self.total_tweets = len(self.tweets)
        self.total_words = self.get_total_words()
        self.total_tokens = self.get_total_tokens()

    def get_total_words(self):
        total_words = 0
        for tweet in self.tweets:
            for sentence in tweet.sentences:
                total_words += len(sentence.words)
        return total_words

    def get_total_tokens(self):
        total_tokens = []
        for tweet in self.tweets:
            for sentence in tweet.sentences:
                total_tokens += sentence.tokens
        return len(list(dict.fromkeys(total_tokens)))

    def write_on_file(self, file):
        file.write("Total Tweets: " + str(self.total_tweets) + '\n')
        file.write("Total Words: " + str(self.total_words) + '\n')
        file.write("Total Tokens: " + str(self.total_tokens) + '\n')
        tweet_index = 1
        for tweet in self.tweets:
            file.write(str(tweet_index) + "." + '\n')
            file.write(tweet.raw_tweet + '\n')
            file.write("--------------------------------------" + '\n')
            tweet_index += 1
