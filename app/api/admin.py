from flask import jsonify,request
from . import api
from app.models import cxf_user,cxf_metas,cxf_relationships
from app.models import db
from app.common import trueReturn,falseReturn
from app.utils.commonOrm import insert,update,delete

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
    user['stuNum'] = u.stu_num

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


#创建新用户
@api.route('/admin/addUser')
def adduser():

    name = request.args.get('name').strip()
    stuNum = request.args.get('stuNum') or None
    point = request.args.get('point') or 55

    u = cxf_user(name=name,stu_num=stuNum,now_point=point,group=0)
    insert(u)
    return jsonify(trueReturn('null','添加成功'))

#修改用户信息
@api.route('/admin/updateUser')
def updateUser():

    uid = request.args.get('uid')
    name = request.args.get('name')
    stuNum = request.args.get('stuNum') or None
    point = request.args.get('point') or 55

    u = cxf_user.query.filter_by(uid=uid).first_or_404()
    u.name = name
    u.stuNum = stuNum
    u.now_point = point
    update()
    return jsonify(trueReturn("null","修改成功!"))

#删除用户
@api.route('/admin/delUser')
def deluser():
    try:
        uid = request.args.get('uid')

        #通过uid找到所有mid
        query = cxf_relationships.query.filter_by(uid=uid).all()

        # 解除关系
        for res in query:
            delete(res)
        #删除用户
        u = cxf_user.query.filter_by(uid=uid).first()
        delete(u)
        return jsonify(trueReturn('null','删除成功!'))
    except:
        return jsonify(falseReturn('null','删除失败!服务器发生了未知错误!'))


#写入action事件
@api.route('/admin/addAction')
def addAction():

    uid = request.args.get('uid')
    action = request.args.get('value')
    action_score = request.args.get('point')
    timeStamp = request.args.get('date')

    print(uid,action,action_score,timeStamp)

    #插入到metas,拿到相应的mid
    m = cxf_metas(action=action,action_score=action_score,time=timeStamp)
    insert(m)
    mid = m.mid
    #添加关系
    rea = cxf_relationships(uid=uid,mid=mid)
    insert(rea)

    #计算分数
    u = cxf_user.query.filter_by(uid=uid).first()
    u.now_point = u.now_point+int(action_score)
    update()

    return jsonify(trueReturn('',"添加事件成功!"))