from flask import jsonify,request
from . import api
from app.models import cxf_user,cxf_metas,cxf_relationships
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



#得到用户的信息
@api.route('/admin/getUserInfo')
def getUserInfo():
    id = request.args.get('id')
    u = cxf_user.query.filter_by(uid=id).first_or_404()
    user = dict()
    user['id'] = u.uid
    user['username'] = u.name
    user['point'] = u.now_point

    return jsonify(trueReturn(data=user,msg='请求成功'))

#得到用户所对应的活动信息
@api.route('/admin/getUserAction')
def getUserAction():
    id = request.args.get('id')
    mid_list = list()
    action_list = list()
    query = cxf_relationships.query.filter_by(uid=id).all()
    for res in query:
        mid_list.append(res.mid)
    for mid in mid_list:
        q = cxf_metas.query.filter_by(mid=mid).first()
        t = dict()
        t['mid'] = q.mid
        t['action'] = q.action
        t['action_score'] = q.action_score
        t['time'] = q.time
        action_list.append(t)
    return jsonify(trueReturn(data=action_list,msg="请求成功!"))