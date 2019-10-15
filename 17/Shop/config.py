# -*- coding=utf-8 -*-
import os
class Config:
    SECRET_KEY = 'mrsoft'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        '''初始化配置文件'''
        pass

# the config for development
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ironman:TonyStark@176.140.8.20:3306/shop'
    DEBUG = True
    host = "176.140.8.20"
    port = 5000


# define the config
config = {
    'default': DevelopmentConfig
}
