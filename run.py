from flask import Flask, request, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import pymysql
import time

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.secret_key = 'shop'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@localhost:3306/shop"
# 设置自动追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 自动提交数据到数据库
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 创建SQLAlchemy实例
db = SQLAlchemy(app)


class Role(db.Model):
    """
    用户权限
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)

    # 添加映射
    users = db.relationship('User',backref='role')

    def __repr__(self):
        return '<User %r' % self.name


class User(db.Model):
    """
    用户表
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    # 引用roles表的数据
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, name, password, role_id=2):
        self.name = name
        self.password = password
        self.role_id = role_id

    def __repr__(self):
        return '<User %r' % self.name


# db.drop_all()
db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form.get('name')
        password = request.form.get('password')
        user = User.query.filter_by(name=name).first()
        if user is not None:
            if user.password == password:
                return render_template('index.html')
        flash('用户名或密码错误')
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if not all([name, password1, password2]):
            flash(u'用户名或者密码为空')
        elif password1 != password2:
            flash(u'两次输入的密码不一致')
        else:
            user = User(name, password1)
            db.session.add(user)
            flash(u'注册成功,3秒后跳转到登录页面')
            time.sleep(1)
            flash(u'注册成功,2秒后跳转到登录页面')
            time.sleep(1)
            flash(u'注册成功,1秒后跳转到登录页面')
            time.sleep(1)
            flash(u'注册成功,0秒后跳转到登录页面')
            return render_template('login.html')
        return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
