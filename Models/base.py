from Models.database import db
from sqlalchemy.orm import Query

class TableBase(object):
    query = None

    @staticmethod
    def init(className):
        className.query = Query(className)

    @staticmethod
    def create_table():
        db.createTable()

    @staticmethod 
    def add(self):
        db.session.add(self)
        db.session.commit()

