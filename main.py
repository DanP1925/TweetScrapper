import csv
from datetime import timedelta, date
from os import listdir

from day_tweets import DayTweets
from party import Party
from summary_detail import SummaryDetail
from summary_generator import SummaryGeneratorFactory
from utils import Utils

SUMMARY_DETAIL = SummaryDetail.TWEET_NUMBERS
CAMPAIGN_END_DATE = date(2016, 1, 1)
CAMPAIGN_START_DATE = date(2015, 9, 1)


def main():
    obtain_all_tweets(CAMPAIGN_START_DATE, CAMPAIGN_END_DATE)
    convert_tweets_to_csv()
    summary_generator = SummaryGeneratorFactory.create_summary_generator(SUMMARY_DETAIL)
    summary_generator.generate_summary()


def obtain_all_tweets(start_date, end_date):
    for party in Party:
        for single_date in date_range(start_date, end_date):
            party.obtain_tweets_for(single_date)


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def convert_tweets_to_csv():
    file_names = listdir("output")
    csv_file_names = listdir("output_csv")
    for file_name in file_names:
        if not Utils.is_text_file(file_name) or is_already_converted(file_name, csv_file_names):
            continue
        with open("./output/" + file_name, "r", encoding="utf-8") as file:
            day_tweet = DayTweets.read_from_file(Party.get_from(file_name), file)


def is_already_converted(raw_file_name, raw_csv_file_names):
    file_name = raw_file_name[:-4]
    csv_file_names = list(map(lambda x: x[:-4], raw_csv_file_names))
    return file_name in csv_file_names


if __name__ == "__main__":
    main()
