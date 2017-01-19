# scolding-bot

스터디 과제 수행을 독려하기 위해 처음 만드는 파이썬 봇.



## PIP

파이썬 패키지 관리를 위한 pip  설치. 커맨드 라인에서 따로 패키지를 `install` 하지 않고 Pycharm IDE를 통해 필요한 패키지 인스톨.

```shell
$ sudo easy_install pip
```



## Heroku [[site](https://www.heroku.com/)]

봇을 배포 할 PaaS ([가격정책](https://www.heroku.com/pricing))

- 회원가입
- CLI 설치

```shell
$ heroku login
# 튜토리얼 문서에서는 heroku create를 통해 랜덤한 이름의 레파지토리를 생성하는데, 직접 Heroku 홈페이지에서 scolding-bot 이라는 이름의 앱 레파지토리를 생성

$ heroku git:clone -a scolding-bot
$ cd scolding-bot
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```

- [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python#introduction) Documents 참고.




# 사용법

1.먼저 [슬랙](https://iamkyu.slack.com/apps/build) 에서 토큰을 발급받아야 하며, Heroku 를 통해 애플리케이션을 배포 합니다. 이에 대한 자세한 내용은 생략합니다. 



2.로컬로 코드를 내려 받습니다.

```shell
$ git clone https://github.com/iamkyu/scolding-bot.git
```



3.`bot.py` 파일과 같은 디렉토리에 `slack.ini` 파일을 생성하고, 형식에 맞춰 데이터를 입력합니다.

```ini
[slack]
token: YOUR-SLACK-TOKEN-ID


[data]
messages  = [
    "메세지1 ( ͡° ͜ʖ ͡°)",
    "메세지2 ( ͡° ͜ʖ ͡°)",
    "메세지3 ( ͡° ͜ʖ ͡°)",
    "메세지4 ( ͡° ͜ʖ ͡°)",
    ]
```

등록한 메세지 중 하나를 선택하여 발송합니다.



4.메세지를 발송할 스케쥴을 정합니다. `bot.py` 파일의 `@sched.scheduled_job` 부분을 찾아 수정합니다.

```python
# 보기1. 특정기간의 특정시간에 메세지를 발송. 아래의 예시는 월요일부터 일요일 오후 5시에 메세지를 발송.
@sched.scheduled_job('cron', day_of_week='mon-sun', hour=17)

# 보기2. 특정간격으로 메세지를 계속발송. 아래의 예시는 3분 간격으로 메세지를 계속 발송.
@sched.scheduled_job('interval', minutes=3)
```

좀 더 자세한 내용은  [Scheduled Jobs with Custom Clock Processes in Python with APScheduler](https://devcenter.heroku.com/articles/clock-processes-python) 문서를 참고 합니다.



# 참고 

- [slacker로 slack bot 만들기](https://hyesun03.github.io/2016/10/08/slackbot/)
- [일일커밋 알림봇 개발기](https://mingrammer.com/dev-commit-alarm-bot)
- [lazy-check-bot](https://github.com/maxtortime/lazy-check-bot)

