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
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ironman:TonyStark@176.140.8.20:3306/shop'
=======
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/shop'
>>>>>>> 480ecbcf9771493317c58132422f5d3934c59bd1
    DEBUG = True
    host = "176.140.8.20"
    port = 5000


# define the config
config = {
    'default': DevelopmentConfig
}
