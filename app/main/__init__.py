from flask import Blurprint

main = Blueprint('main', __name__)

# 避免循环导入依赖
from . import views, errors