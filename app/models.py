from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class cxf_admin(db.Model):

    __tablename__ = 'cxf_admin'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32))
    password = db.Column(db.String(64))


class cxf_user(db.Model):

    __tablename__ = 'cxf_user'

    uid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32))
    stu_num = db.Column(db.String(32))
    now_point = db.Column(db.Integer)


class cxf_relationships(db.Model):

    __tablename__ = 'cxf_relationships'

    cid = db.Column(db.Integer,primary_key=True,nullable=False)
    mid = db.Column(db.Integer,primary_key=True,nullable=False)

class cxf_metas(db.Model):

    __tablename__ = 'cxf_metas'

    mid = db.Column(db.Integer,primary_key=True,nullable=False)
    action = db.Column(db.TEXT)
    action_score = db.Column(db.Integer)
    time = db.Column(db.Integer)

class cxf_options(db.Model):

    __tablename__ = 'cxf_options'

    name = db.Column(db.String(32),primary_key=True,nullable=False)
    value = db.Column(db.Text,default="NULL")