import os

'''程序的配置文件'''

# 程序的绝对文件位置
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    pass


# 基类 Config 中包含通用配置，子类分别定义专用的配置。如果需要，你还可添加其他配置类。
class DevelopmentConfig(Config):

    SECRET_KEY = os.environ.get('SECRET_KEY') or "hard_to_guess"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/cxfsys'



class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or "hard_to_guess"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/cxfsys'
configs = {
    "development":DevelopmentConfig,
    "production":ProductionConfig
}