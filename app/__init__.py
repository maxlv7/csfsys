from flask import Flask
from config import configs
from app.models import db
from app.utils import init_errors,init_utils
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    with app.app_context():

        # 允许跨域
        CORS(app)
        #导入配置
        app.config.from_object(configs['development'])

        #初始化数据库
        db.init_app(app)

        #创建数据表
        db.create_all()

        #初始化错误处理
        init_errors(app)

        #初始化工具
        init_utils(app)

        #注册api
        from app.api import api
        app.register_blueprint(api)

        return app
