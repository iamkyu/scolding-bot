# coding: utf-8
from slacker import Slacker
from ConfigParser import SafeConfigParser
from apscheduler.schedulers.blocking import BlockingScheduler

import datetime
import pytz
import random

sched = BlockingScheduler()
timezone = pytz.timezone('Asia/Seoul')
channels = ['#random']
messages = [
    u'>\n..? 자니? 스터디 과제는 다했구? ( ͡° ͜ʖ ͡°)',
    u'>\n웅? 스터디 복습은 다 하고 티비 보고 있는 거야? ( ͡° ͜ʖ ͡°)ㅎ',
    u'>\n공부해야한다.\n공부해야한다.\n공부해야한다',
    u'>\n하라는 스터디 과제는 안하고ㅎ 넝담~ㅎ',
    u'>\n심심한데 조쉬롱 아저씨 라이브 코딩이나 볼까ㅎ\nhttps://www.youtube.com/watch?v=fxB0tVnAi0I'
]


def get_slack_token():
    parser = SafeConfigParser()
    parser.read('slack.ini')
    return parser.get('slack', 'token')


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
    slacker.chat.post_message(channels[0], random.choice(messages), as_user=True)


if __name__ == '__main__':
    sched.start()