from flask import request,abort
from flask import jsonify
from app.auth import Auth
from app.common import trueReturn,falseReturn

def init_errors(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify(falseReturn('null','找不到资源'))

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify(falseReturn('null', '没有权限'))

    @app.errorhandler(500)
    def general_error(error):
        return jsonify(falseReturn('null', '服务器错误'))

    @app.errorhandler(502)
    def gateway_error(error):
        return jsonify(falseReturn('null', '网关出错'))

def init_utils(app):

    @app.before_request
    def judge():
        #权限验证，解析Token
        #如果访问管理页面
        if(request.path.startswith('/api/admin')):
            try:
                Token = request.headers.get('Authorization')
                #解析token
                data = Auth.decode_token(Token)
                print(data)
                #在这里判断是否为管理员
                if(data['data']['group']!=1):
                    abort(403)
            except:
                abort(403)





