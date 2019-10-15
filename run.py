from flask import Flask, request, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import pymysql
import time
from datetime import datetime

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


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    username = db.Column(db.String(100)) # 用户名
    password = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号
    consumption = db.Column(db.DECIMAL(10, 2), default=0)  # 消费额
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    orders = db.relationship('Orders', backref='user')  # 订单外键关系关联

    def __repr__(self):
        return '<User %r>' % self.name

    def check_password(self, password):
        """
        检测密码是否正确
        :param password: 密码
        :return: 返回布尔值
        """
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)

# 管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    manager = db.Column(db.String(100), unique=True)  # 管理员账号
    password = db.Column(db.String(100))  # 管理员密码

    def __repr__(self):
        return "<Admin %r>" % self.manager

    def check_password(self, password):
        """
        检测密码是否正确
        :param password: 密码
        :return: 返回布尔值
        """
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)

# 大分类
class SuperCat(db.Model):
    __tablename__ = "supercat"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    cat_name = db.Column(db.String(100))  # 大分类名称
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    subcat = db.relationship("SubCat", backref='supercat')  # 外键关系关联
    goods = db.relationship("Goods", backref='supercat')  # 外键关系关联

    def __repr__(self):
        return "<SuperCat %r>" % self.cat_name

# 子分类
class SubCat(db.Model):
    __tablename__ = "subcat"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    cat_name = db.Column(db.String(100))  # 子分类名称
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    super_cat_id = db.Column(db.Integer, db.ForeignKey('supercat.id'))  # 所属大分类
    goods = db.relationship("Goods", backref='subcat')  # 外键关系关联

    def __repr__(self):
        return "<SubCat %r>" % self.cat_name


# 商品
class Goods(db.Model):
    __tablename__ = "goods"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(255))  # 名称
    original_price = db.Column(db.DECIMAL(10,2))  # 原价
    current_price  = db.Column(db.DECIMAL(10,2))  # 现价
    picture = db.Column(db.String(255))  # 图片
    introduction = db.Column(db.Text)  # 商品简介
    views_count = db.Column(db.Integer,default=0) # 浏览次数
    is_sale  = db.Column(db.Boolean(), default=0) # 是否特价
    is_new = db.Column(db.Boolean(), default=0) # 是否新品

    # 设置外键
    supercat_id = db.Column(db.Integer, db.ForeignKey('supercat.id'))  # 所属大分类
    subcat_id = db.Column(db.Integer, db.ForeignKey('subcat.id'))  # 所属小分类
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    cart = db.relationship("Cart", backref='goods')  # 订单外键关系关联
    orders_detail = db.relationship("OrdersDetail", backref='goods')  # 订单外键关系关联

    def __repr__(self):
        return "<Goods %r>" % self.name

# 购物车
class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    goods_id = db.Column(db.Integer, db.ForeignKey('goods.id'))  # 所属商品
    user_id = db.Column(db.Integer)  # 所属用户
    number = db.Column(db.Integer, default=0)  # 购买数量
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    def __repr__(self):
        return "<Cart %r>" % self.id

# 订单
class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    recevie_name = db.Column(db.String(255))  # 收款人姓名
    recevie_address = db.Column(db.String(255))  # 收款人地址
    recevie_tel = db.Column(db.String(255))  # 收款人电话
    remark = db.Column(db.String(255))  # 备注信息
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    orders_detail = db.relationship("OrdersDetail", backref='orders')  # 外键关系关联
    def __repr__(self):
        return "<Orders %r>" % self.id

class OrdersDetail(db.Model):
    __tablename__ = 'orders_detail'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    goods_id = db.Column(db.Integer, db.ForeignKey('goods.id'))  # 所属商品
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))  # 所属订单
    number = db.Column(db.Integer, default=0)  # 购买数量


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
    app.run(debug=True,host="176.140.8.20",port=5000)
