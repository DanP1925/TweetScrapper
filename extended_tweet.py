from nltk import sent_tokenize

from sentence import Sentence


class ExtendedTweet:

    def __init__(self, tweet):
        self.raw_tweet = tweet
        self.sentences = list(map(lambda sentence: Sentence(sentence), sent_tokenize(self.raw_tweet)))
