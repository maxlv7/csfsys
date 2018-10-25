from app.models import db

def insert(data):
    db.session.add(data)
    db.session.commit()

def update():
    db.session.commit()

def delete(data):
    db.session.delete(data)
    db.session.commit()