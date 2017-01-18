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



# 참고

- [slacker로 slack bot 만들기](https://hyesun03.github.io/2016/10/08/slackbot/)
- [일일커밋 알림봇 개발기](https://mingrammer.com/dev-commit-alarm-bot)
- [lazy-check-bot](https://github.com/maxtortime/lazy-check-bot)
- [Scheduled Jobs with Custom Clock Processes in Python with APScheduler](https://devcenter.heroku.com/articles/clock-processes-python)

