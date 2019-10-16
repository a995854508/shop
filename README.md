# 网上商城

#### 需求分析:
##### 使用MySQL和flask实现,所有功能需和数据库互联,需要网页交互
#### 创建数据库shop,通过flask连接数据库,使用flask建表

##### 1.用户注册,登录,退出,修改个人信息
注册模块概述:实现用户成为网站的会员功能。在注册界面中，用户需要填写会员信息，然后单击“同意协议并注册”，程序将自动验证是否唯一，如果唯一，则保存在数据库中，否则提示修改。最终运行结果类似

图1.1会员注册页面运行结果
注册页面模块功能实现
创建注册页面表单－>显示注册页面－>验证并保存注册信息
登录模块概述:在该页面中，填写会员账号,密码和验证码，单击登录按钮即可实现会员的登录，输入出错则给予提示，效果图如下:


登录页面模块功能实现
生成验证码－>显示验证码－>检验证码->保存会员登录状态
会员退出功能：清空Session中的user_id和username



##### 2.首页商品图片轮播展示,显示热销和推荐购买,搜索商品(万松)
显示商品热销(根据商品销量),显示商品推荐(根据用户搜索或者浏览),每个商品图片
需要有一个链接,用于跳转到商品详情页,右上角有登录|注册,登录成功有用户头像,
用户点击可以查看用户信息,并可以退出登录.正上方有搜索框,可以搜索商品,可以根
据商品名称关键字搜索商品,跳转到一个类似首页但没有轮播展示,可以下拉的包含所有
符合条件商品的页面,没有相关商品则返回'未找到相关商品'.

##### 3.查看商品详细信息,加入购物车,清空购物车,加减商品数量（吴谦）
商品详情页(一个框架,包含商品图片,商品价格,加入购物车按钮)
购物车页面:显示用户所有购物车商品,可以加减或者移除,选中部分或者所有商品提交订
单,提交成功跳转到支付页面

##### 4.提交订单,设置默认收货地址,显示支付宝二维码,查看订单详情(余以晨)
支付页面:若没有设置收货地址,则必须填写地址,有则显示默认地址,可以修改地址,点击
提交弹出支付宝二维码(意思意思),再点击二维码下方提交跳转到成功界面,点击取消则返
回支付页面,再点击取消返回购物车页面
订单详情页面:查看订单详情

##### 5.用户管理,可以查看,删除,更改所有用户信息,可以查看所有订单信息(张家豪)
登录管理员账号跳转到此页,可以搜索查看某个用户的信息,可以修改用户的状态(正常,冻
结,注销),可以选择删除已注销用户.可以添加用户.可以查看所有订单信息.

##### 6.商品管理,可以查看,删除,更改所有商品信息,可以查看商品销量排行(周祖坤)
登录店家账号跳转到此页(目前先假设只有一家店).
商品至少包含图片,价格属性.

#### 初步产品需求,欢迎各位修改,每个人选一个,先到先得,你们商量一下,我选剩下的
#### 数据库表包含用户表
### 数据备份
#### 1. 备份命令格式
mysqldump -u root -p shop > ./shop.sql(保存在当前文件夹)

#### 2. 恢复命令格式
mysql -u root -p shop < shop.sql(恢复当前文件夹的shop数据库)
<<<<<<< HEAD
=======


一、安装环境介绍

　　需要预先安装gcc，通常ubuntu默认自带，所以默认已经有这个环境了，后续步骤默认是使用root账户进行的

二、下载及安装nginx相关组件

　　1、进入任意目录，我选用的是通常选用的/usr/local/src目录

cd /usr/local/src
　　2、下载相关组件

wget http://nginx.org/download/nginx-1.10.2.tar.gz
wget http://www.openssl.org/source/openssl-fips-2.0.10.tar.gz
wget http://zlib.net/zlib-1.2.11.tar.gz
wget ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.40.tar.gz
　　3、安装nginx相关组件

　　安装openssl

tar zxvf openssl-fips-2.0.10.tar.gz
cd openssl-fips-2.0.10
./config && make && make install
　　安装pcre

tar zxvf pcre-8.40.tar.gz
cd pcre-8.40
./configure && make && make install
　　安装zlib

tar zxvf zlib-1.2.11.tar.gz
cd zlib-1.2.11
./configure && make && make install
　　4、安装nginx

tar zxvf nginx-1.10.2.tar.gz
cd nginx-1.10.2
./configure && make && make install
三、启动nginx

　　1、启动nginx

/usr/local/nginx/sbin/nginx
　　2、查看nginx是否启动成功

netstat -lnp
　　3、基本操作

/usr/local/nginx/sbin/nginx#启动
/usr/local/nginx/sbin/nginx -s stop(quit、reload)#停止/重启
/usr/local/nginx/sbin/nginx -h#命令帮助
vi /usr/local/nginx/conf/nginx.conf#配置文件
四、nginx负载均衡配置

　　1、打开配置文件

vi /usr/local/nginx/conf/nginx.conf
　　2、配置相关配置项

复制代码
upstream xxx{};upstream模块是命名一个后端服务器组，组名必须为后端服务器站点域名，内部可以写多台服务器ip和port，还可以设置跳转规则及权重等等
ip_hash;代表使用ip地址方式分配跳转后端服务器，同一ip请求每次都会访问同一台后端服务器
server;代表后端服务器地址

server{};server模块是接收外部请求的部分
server_name;代表外网访问域名
location / {};同样代表过滤器，用于制定不同请求的不同操作
proxy_pass;代表后端服务器组名，此组名必须为后端服务器站点域名



然后就可以直接使用ip+端口去访问了

搞定！
>>>>>>> aa50ae9666d023b5cfcf95ae662dccc8da20d40d
