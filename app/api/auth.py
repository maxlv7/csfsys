from . import api
from flask import jsonify
from flask import request
from app.auth import Auth
from app.models import cxf_user
from app.common import falseReturn

@api.route('/test',methods=['POST'])
def test():
    return jsonify(a=1,b=2)



@api.route('/auth/login',methods=["GET","POST"])
def login():
    res = request.get_json()
    try:
        # 得到用户信息
        username = res.get('username')
        password = res.get('password')

        #查询数据库，是否正确
        user = cxf_user.query.filter_by(name=username).first()
        if user:
            if user.password == password:
                u_id = user.uid
                u_name = user.name
                u_group = user.group
                #包装jwt,uid为查询后的uid,username为username
                token = Auth.encode_token(uid=u_id,username=u_name,group=u_group)

                json = {
                    'msg':'登录成功!',
                    'data':{
                        'token':token,
                        'uid':u_id,
                        'username':u_name,
                        'group':u_group
                    },
                    'status':200
                }

                return jsonify(json)
            else:
                return jsonify(falseReturn("null","密码错误!"))
        else:
            return jsonify(falseReturn("null","没有此用户!"))
    except Exception as e:
        pass

    return jsonify(falseReturn("null", "未知错误!"))