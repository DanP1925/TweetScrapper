from os import path, stat


class ExtendedFile:

    def __init__(self, name, date):
        self.file_name = "./output/" + name + "_" + date.strftime('%Y_%m_%d') + ".txt"

    def has_tweets(self):
        return not self.exist() or (self.exist() and self.is_empty())

    def exist(self):
        return path.exists(self.file_name)

    def is_empty(self):
        return stat(self.file_name).st_size == 0
