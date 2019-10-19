from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql://root:123456@localhost:3306/shop'
# 设置自动追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 自动提交数据到数据库
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


class Admin(db.Model):
    """
    管理员表
    """
