from sqlalchemy import Column, Integer, String, Date
from Models.database import db
from Models.base import TableBase

class Loan(db.Base, TableBase):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key = True)
    type = Column(String(50))
    amount = Column(Integer)

    def __repr__(self):
        return '<Loan: {0}, type: {1}'.format(id, type)
