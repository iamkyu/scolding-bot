# coding: utf-8

from slacker import Slacker
from ConfigParser import SafeConfigParser
from apscheduler.schedulers.blocking import BlockingScheduler

import datetime
import pytz
import random
import codecs
import json

logging.basicConfig()
sched = BlockingScheduler()
timezone = pytz.timezone('Asia/Seoul')
parser = SafeConfigParser()
parser.readfp(codecs.open('slack.ini', 'r', 'utf8'))

channels = ['#random']
last_send_msg_idx = 0


def get_slack_token():
    return parser.get('slack', 'token')


def get_message():
    global last_send_msg_idx
    messages = json.loads(parser.get('data', 'messages'))
    while True:
        rand_msg_idx = random.randrange(0, len(messages))
        if rand_msg_idx != last_send_msg_idx:
            last_send_msg_idx = rand_msg_idx
            break
    return messages[rand_msg_idx]


def get_today_of_week():
    return datetime.datetime.isoweekday(datetime.datetime.now(timezone))


def get_sending_time(day):
    is_weekend = day >= 6
    hour_from = 13 if is_weekend else 19
    hour_to = 22
    sending_time = random.randrange(hour_from, hour_to)
    return sending_time


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=get_sending_time(get_today_of_week()))
def main():
    slacker = Slacker(get_slack_token())
    slacker.chat.post_message(channels[0], get_message(), as_user=True)

if __name__ == '__main__':
    sched.start()
