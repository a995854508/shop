from wtforms.validators import DataRequired, Email, Regexp, \
    EqualTo, ValidationError, Length
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, \
    TextAreaField, RadioField, DecimalField, SelectField

from app.model import *


class RegisterForm(FlaskForm):
    """
    用户注册表单
    """
    username = StringField(
        label="账户 ：",
        validators=[
            DataRequired("用户名不能为空！"),
            Length(min=3, max=50, message="用户名长度必须在3到10位之间")
        ],
        description="用户名",
        render_kw={
            "type": "text",
            "placeholder": "请输入用户名！",
            "class": "validate-username",
            "size": 38,
        }
    )
    phone = StringField(
        label="联系电话 ：",
        validators=[
            DataRequired("手机号不能为空！"),
            Regexp("1[34578][0-9]{9}", message="手机号码格式不正确")
        ],
        description="手机号",
        render_kw={
            "type": "text",
            "placeholder": "请输入联系电话！",
            "size": 38,
        }
    )
    email = StringField(
        label="邮箱 ：",
        validators=[
            DataRequired("邮箱不能为空！"),
            Email("邮箱格式不正确！")
        ],
        description="邮箱",
        render_kw={
            "type": "email",
            "placeholder": "请输入邮箱！",
            "size": 38,
        }
    )
    password = PasswordField(
        label="密码 ：",
        validators=[
            DataRequired("密码不能为空！")
        ],
        description="密码",
        render_kw={
            "placeholder": "请输入密码！",
            "size": 38,
        }
    )
    repassword = PasswordField(
        label="确认密码 ：",
        validators=[
            DataRequired("请输入确认密码！"),
            EqualTo('password', message="两次密码不一致！")
        ],
        description="确认密码",
        render_kw={
            "placeholder": "请输入确认密码！",
            "size": 38,
        }
    )
    submit = SubmitField(
        '同意协议并注册',
        render_kw={
            "class": "btn btn-primary login",
        }
    )

    def validate_email(self, field):
        """
        检测注册邮箱是否已经存在
        :param field: 字段名
        """
        email = field.data
        user = User.query.filter_by(email=email).count()
        if user == 1:
            raise ValidationError("邮箱已经存在！")

    def validate_phone(self, field):
        """
        检测手机号是否已经存在
        :param field: 字段名
        """
        phone = field.data
        user = User.query.filter_by(phone=phone).count()
        if user == 1:
            raise ValidationError("手机号已经存在！")


class LoginForm(FlaskForm):
    """
    登录功能
    """
    username = StringField(
        validators=[
            DataRequired("用户名不能为空！"),
            Length(min=3, max=50, message="用户名长度必须在3到10位之间")
        ],
        description="用户名",
        render_kw={
            "type": "text",
            "placeholder": "请输入用户名！",
            "class": "validate-username",
            "size": 38,
            "maxlength": 99
        }
    )
    password = PasswordField(
        validators=[
            DataRequired("密码不能为空！"),
            Length(min=3, message="密码长度不少于6位")
        ],
        description="密码",
        render_kw={
            "type": "password",
            "placeholder": "请输入密码！",
            "class": "validate-password",
            "size": 38,
            "maxlength": 99
        }
    )
    verify_code = StringField(
        'VerifyCode',
        validators=[DataRequired()],
        render_kw={
            "class": "validate-code",
            "size": 18,
            "maxlength": 4,
        }
    )

    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-primary login",
        }
    )


class PasswordForm(FlaskForm):
    """
     修改密码表单
     """
    old_password = PasswordField(
        label="原始密码 ：",
        validators=[
            DataRequired("原始密码不能为空！")
        ],
        description="原始密码",
        render_kw={
            "placeholder": "请输入原始密码！",
            "size": 38,
        }
    )
    password = PasswordField(
        label="新密码 ：",
        validators=[
            DataRequired("新密码不能为空！")
        ],
        description="新密码",
        render_kw={
            "placeholder": "请输入新密码！",
            "size": 38,
        }
    )
    repassword = PasswordField(
        label="确认密码 ：",
        validators=[
            DataRequired("请输入确认密码！"),
            EqualTo('password', message="两次密码不一致！")
        ],
        description="确认密码",
        render_kw={
            "placeholder": "请输入确认密码！",
            "size": 38,
        }
    )
    submit = SubmitField(
        '确认修改',
        render_kw={
            "class": "btn btn-primary login",
        }
    )

    def validate_old_password(self, field):
        from flask import session
        old_password = field.data
        user_id = session["user_id"]
        user = User.query.get(int(user_id))
        if not user.check_password(old_password):
            raise ValidationError("原始密码错误！")


class SuggetionForm(FlaskForm):
    """
    意见建议
    """
    name = StringField(
        label="姓名",
        validators=[
            DataRequired("姓名不能为空！")
        ],
        description="姓名",
        render_kw={
            "placeholder": "请输入姓名！",
            "class": "form-control"
        }
    )
    email = StringField(
        label="邮箱",
        validators=[
            DataRequired("邮箱不能为空！")
        ],
        description="邮箱",
        render_kw={
            "type": "email",
            "placeholder": "请输入邮箱！",
            "class": "form-control"
        }
    )
    content = TextAreaField(
        label="意见建议",
        validators=[
            DataRequired("内容不能为空！")
        ],
        description="意见建议",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入内容！",
            "rows": 7
        }
    )
    submit = SubmitField(
        '发送消息',
        render_kw={
            "class": "btn-default btn-cf-submit",
        }
    )


class MLoginForm(FlaskForm):
    """
    管理员登录表单
    """
    manager = StringField(
        label="管理员名",
        validators=[
            DataRequired("管理员名不能为空")
        ],
        description="管理员名",
        render_kw={
            "class": "manager",
            "placeholder": "请输入管理员名！",
        }
    )
    password = PasswordField(
        label="密码",
        validators=[
            DataRequired("密码不能为空")
        ],
        description="密码",
        render_kw={
            "class": "password",
            "placeholder": "请输入密码！",
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "login_ok",
        }
    )

    # 验证账号，命名规则：validate_ + 字段名。如果要验证密码，则可以创建函数validate_pwd
    def validate_manager(self, field):
        account = field.data
        admin = Admin.query.filter_by(manager=account).count()
        if admin == 0:
            raise ValidationError("账号不存在! ")


class GoodsForm(FlaskForm):
    name = StringField(
        label="商品名称",
        validators=[
            DataRequired("商品名称不能为空！"),
        ],
        description="商品名称",
        render_kw={
            "class": "Sytle_text",
            "placeholder": "请输入商品名称！",
            "size": "50"
        }
    )
    supercat_id = SelectField(
        label="大分类",
        validators=[
            DataRequired("请选择大分类！")
        ],
        coerce=int,
        description="大分类",
        render_kw={
            "class": "form-control",
        }
    )

    subcat_id = SelectField(
        label="小分类",
        validators=[
            DataRequired("请选择小分类！")
        ],
        coerce=int,
        description="小分类",
        render_kw={
            "class": "form-control",
        }
    )
    picture = StringField(
        label="图片名称",
        validators=[
            DataRequired("图片名称不能为空！")
        ],
        description="图片名称",
        render_kw={
            "class": "Style_upload",
            "placeholder": "请输入图片名称！"
        }
    )
    original_price = DecimalField(
        label="商品价格",
        validators=[
            DataRequired("请输入正确的价格类型")
        ],
        description="商品价格",
        render_kw={
            "class": "Sytle_text",
            "placeholder": "请输入商品价格！"
        }
    )
    current_price = DecimalField(
        label="商品现价",
        validators=[
            DataRequired("商品现价不能为空！")
        ],
        description="商品现价",
        render_kw={
            "class": "Sytle_text",
            "placeholder": "请输入商品现价！"
        }
    )
    is_new = RadioField(
        label='是否新品',
        description="是否新品",
        coerce=int,
        choices=[(0, '否'), (1, '是')], default=0,
        render_kw={
            "class": "is_radio"
        }
    )
    is_sale = RadioField(
        label='是否特价',
        description="是否特价",
        coerce=int,
        choices=[(0, '否'), (1, '是')], default=0,
        render_kw={
            "class": "is_radio"
        }
    )
    introduction = TextAreaField(
        label=" 商品简介",
        validators=[
            DataRequired(" 商品简介不能为空！")
        ],
        description=" 商品简介",
        render_kw={
            "class": "textarea",
            "rows": 5
        }
    )
    submit = SubmitField(
        '保存',
        render_kw={
            "class": "btn_bg_short",
        }
    )
