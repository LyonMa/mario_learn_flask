# 工厂函数是被用来延迟创建实例，以便解决动态修改配置的问题，且可支持创建多个实例
# 工厂函数是一种特殊的构造函数
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_pagedown import PageDown

# 实例化一些对象(扩展)
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
# login_view 属性用于设置登陆页面的端点
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
pagedown = PageDown()

# 工厂函数
def create_app(config_name):
	app = Flask(__name__)
	# 将config.py中的配置对象，用.from_object()方法导入应用实例
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	bootstrap.init_app(app)
	mail.init_app(app)
	moment.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)
	pagedown.init_app(app)

	# 导入、注册蓝本
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	# 导入、注册身份验证蓝本
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='/auth')

	return app