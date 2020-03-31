from extended_tweet import ExtendedTweet


class DayTweets:
    SEPARATOR = "--------------------------------------"

    def __init__(self, party, tweets):
        self.party = party
        self.tweets = tweets
        self.total_tweets = len(self.tweets)
        self.total_words = self.get_total_words()
        self.tokens = self.get_tokens()
        self.total_tokens = len(self.get_tokens())

    @staticmethod
    def read_from_file(party, file):
        file.readline()
        file.readline()
        file.readline()

        raw_tweets = []
        lines = file.readlines()
        has_read_tweet_index = False
        raw_tweet = ""
        for line in lines:
            if not has_read_tweet_index:
                has_read_tweet_index = True
                continue
            elif line == DayTweets.SEPARATOR + '\n':
                raw_tweets.append(raw_tweet)
                has_read_tweet_index = False
                raw_tweet = ""
            else:
                raw_tweet += line

        return DayTweets(party, list(map(lambda raw_tweet: ExtendedTweet(raw_tweet), raw_tweets)))

    def get_total_words(self):
        total_words = 0
        for tweet in self.tweets:
            for sentence in tweet.sentences:
                total_words += len(sentence.words)
        return total_words

    def get_tokens(self):
        total_tokens = []
        for tweet in self.tweets:
            for sentence in tweet.sentences:
                total_tokens += sentence.tokens
        return total_tokens

    def write_on_file(self, file):
        file.write("Total Tweets: " + str(self.total_tweets) + '\n')
        file.write("Total Words: " + str(self.total_words) + '\n')
        file.write("Total Tokens: " + str(self.total_tokens) + '\n')
        tweet_index = 1
        for tweet in self.tweets:
            file.write(str(tweet_index) + "." + '\n')
            file.write(tweet.raw_tweet + '\n')
            file.write(self.SEPARATOR + '\n')
            tweet_index += 1
