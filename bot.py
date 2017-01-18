from slacker import Slacker
from ConfigParser import SafeConfigParser
from apscheduler.schedulers.blocking import BlockingScheduler

import datetime
import pytz
import random

sched = BlockingScheduler()
timezone = pytz.timezone('Asia/Seoul')
channels = ['#random']


def get_slack_token():
    parser = SafeConfigParser()
    parser.read('slack.ini')
    return parser.get('slack', 'token')


def post_to_channel(message, idx):
    slack.chat.post_message(channels[idx], message, as_user=True)


def get_today_of_week():
    return datetime.datetime.isoweekday(datetime.datetime.now(timezone))


def get_sending_time(day):
    if day >= 6:
        hour_from = 13
        hour_to = 21
    else:
        hour_from = 19
        hour_to = 22

    return random.randrange(hour_from, hour_to)


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=get_sending_time(get_today_of_week()))
def main():
    slacker = Slacker(get_slack_token())
    slacker.chat.post_message(channels[0], 'message', as_user=True)


if __name__ == '__main__':
    sched.start()
