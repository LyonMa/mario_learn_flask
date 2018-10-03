from flask import Blueprint

main = Blueprint('main', __name__)

# 避免循环导入依赖
from . import views, errors

@main.app_context_processor
def inject_permissions():
	return dict(Permission=Permission)