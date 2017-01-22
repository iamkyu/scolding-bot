# coding: utf-8

from slacker import Slacker
from ConfigParser import SafeConfigParser
from apscheduler.schedulers.blocking import BlockingScheduler

import datetime
import pytz
import random
import codecs
import json
import logging

logging.basicConfig()
sched = BlockingScheduler()
timezone = pytz.timezone('Asia/Seoul')
parser = SafeConfigParser()
parser.readfp(codecs.open('slack.ini', 'r', 'utf8'))

channels = ['#random']


def get_slack_token():
    """ slack.ini 파일에서 슬랙 토큰을 읽어와 반환한다

    :return: 슬랙 토큰
    """
    return parser.get('slack', 'token')


def get_message():
    """ slack.ini 파일에 등록된 메세지를 읽어 그 중 하나를 반환한다

    :return: 등록 된 메세지 리스트 중 하나의 메세지
    """
    messages = json.loads(parser.get('data', 'messages'))
    message = messages[random.randrange(0, len(messages))]
    logging.info('##### message: %s', message)
    return message


def get_day_of_week(day):
    """ 특정 날짜가 일주일 중 몇번째 요일인지 반환한다

    :param day: today or tomorrow
    :return: 해당 요일의 번호 (월요일=1, 화요일=2 ~ 일요일=7)
    """
    if day == 'today':
        number_of_day = datetime.datetime.isoweekday(datetime.datetime.now(timezone))
    else:
        number_of_day = datetime.datetime.isoweekday(datetime.datetime.now(timezone) + datetime.timedelta(days=1))

    return number_of_day


def get_sending_time(day):
    """ 메세지 발송 시간을 랜덤하게 구한다

    :param day: 해당 요일의 번호 (월요일=1, 화요일=2 ~ 일요일=7)
    :return: 평일인경우 19~22사이 / 주말인경우 13~22사이의 숫자
    """
    is_weekend = day >= 6
    hour_from = 13 if is_weekend else 19
    hour_to = 22
    sending_hour = random.randrange(hour_from, hour_to)

    return sending_hour


def set_tomorrow_schedule():
    """ 내일 메세지 발송 스케쥴을 설정한다"""
    number_of_tomorrow = get_day_of_week('tomorrow')
    sending_time = get_sending_time(get_day_of_week(number_of_tomorrow))
    sched.reschedule_job('messaging_job', jobstore=None,
                         trigger='cron',
                         day_of_week=number_of_tomorrow,
                         hour=sending_time)
    print(sending_time)
    logging.info('##### Set tomorrow scheduled at %s', sending_time)


def send_message():
    """ 슬랙채널로 메세지를 발송한다"""
    slacker.chat.post_message(channels[0], get_message(), as_user=True)
    set_tomorrow_schedule()


if __name__ == '__main__':
    slacker = Slacker(get_slack_token())
    tomorrow = get_day_of_week('tomorrow')
    sched.add_job(send_message, 'cron',
                  day_of_week=tomorrow,
                  hour=get_sending_time(tomorrow),
                  id='messaging_job')
    sched.start()
