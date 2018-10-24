from flask import render_template
from . import main

# 为了在全局作用域实现，此处使用app_errorhandler而不是errorhandler
@main.app_errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500