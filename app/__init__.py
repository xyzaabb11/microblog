#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))


from flask_oauthlib.client import OAuth
oauth = OAuth(app)
douban = oauth.remote_app(
        'douban',
        consumer_key = '00db93e0641c8d850292bba12c55a88f',
        consumer_secret = '997d6a75f8e8aca9',
        base_url = 'https://api.douban.com/',
        request_token_url='https://www.douban.com/service/auth2/auth',
        access_token_url='https://www.douban.com/service/auth2/token',
        authorize_url='/oauth2.0/authorize',)
from app import views, models
