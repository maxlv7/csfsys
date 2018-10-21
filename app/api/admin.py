from flask import jsonify
from . import api
from app.models import cxf_user
from app.common import trueReturn,falseReturn

#得到所有信息和分数表
@api.route('/admin/getStuList',methods=["GET"])
def getStuList():
    try:
        all_list = cxf_user.query.all()
        all_info= list()
        for user in all_list:
            info = dict()
            info['id'] = user.uid
            info['name'] = user.name
            info['point'] = user.now_point
            all_info.append(info)
        return jsonify(trueReturn({'stuList':all_info},msg="success"))
    except:
        return jsonify(falseReturn("null",'查询错误!'))