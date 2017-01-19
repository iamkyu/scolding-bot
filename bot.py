# coding: utf-8

from slacker import Slacker
from ConfigParser import SafeConfigParser
from apscheduler.schedulers.blocking import BlockingScheduler

import datetime
import pytz
import random
import codecs
import json

sched = BlockingScheduler()
timezone = pytz.timezone('Asia/Seoul')
parser = SafeConfigParser()
parser.readfp(codecs.open('slack.ini', 'r', 'utf8'))

channels = ['#random']


def get_slack_token():
    return parser.get('slack', 'token')


def get_message():
    messages = json.loads(parser.get('data', 'messages'))
    return messages[random.randrange(0, len(messages))]


def get_today_of_week():
    return datetime.datetime.isoweekday(datetime.datetime.now(timezone))


def get_sending_time(day):
    hour_from = 13 if day >= 6 else 19
    hour_to = 22
    return random.randrange(hour_from, hour_to)


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=get_sending_time(get_today_of_week()))
def main():
    slacker = Slacker(get_slack_token())
    slacker.chat.post_message(channels[0], get_message(), as_user=True)

if __name__ == '__main__':
    sched.start()
