from flask import render_template

from model import *

db.create_all()


@app.route('/')
@app.route('/index')
def index():
    """
    首页
    :return:
    """
    new_goods = Goods.query.filter_by(is_new=1).order_by(
        Goods.addtime.desc()).limit(12).all()
    sale_goods = Goods.query.filter_by(is_sale=1).order_by(
        Goods.addtime.desc()).limit(12).all()
    hot_goods = Goods.query.order_by(
        Goods.views_count.desc()).limit(2).all()
    return render_template('home/index.html',
                           new_goods=new_goods,
                           sale_goods=sale_goods,
                           hot_goods=hot_goods)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
