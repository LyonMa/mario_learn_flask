import os
basedir = os.path.abspath(os.path.dirname(__file__))


class config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
	MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
		['true', 'on', '1']
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.envrion.get('MAIL_PASSWORD')
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = '6777marcus@gmail.com'
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	@staticmethod
	def init_app(app):
		pass


class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data-dev.sqite')


class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.envrion.get('TEST_DATABASE_URL') or \
		'sqlite://'
		# 测试环境中的数据库指向内存，因为其数据不需要被保存


class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.envrion.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data.sqlite')


# 不同环境的配置
config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,

	'default': DevelopmentConfig
}