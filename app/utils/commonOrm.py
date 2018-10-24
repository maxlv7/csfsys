from app.models import db

def insert(data):
    db.session.add(data)
    db.session.commit()