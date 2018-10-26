#一些工具函数
from app.models import cxf_options
from .commonOrm import insert,update

def get_config(key):
    try:
        c = cxf_options.query.filter_by(name=key).first_or_404()
        return c.value
    except:
        return False

def set_config(key,value):

    #如果有这种配置
    if(get_config(key)):
        opt = cxf_options.query.filter_by(name=key).first()
        opt.value = value
        update()
        return True
    else:
        try:
            c = cxf_options(name=key,value=value)
            insert(c)
            return True
        except:
            return False