from nltk import sent_tokenize

from sentence import Sentence


class ExtendedTweet:

    def __init__(self, tweet):
        self.raw_tweet = tweet.text
        self.sentences = map(lambda sentence: Sentence(sentence), sent_tokenize(tweet.text))
