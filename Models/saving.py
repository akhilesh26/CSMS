from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from Models.database import db
from Models.base import TableBase

class Saving(db.Base, TableBase):
    __tablename__ = 'saving'
    #id = Column(Integer, primary_key = True)
    account_no = Column(String(10), primary_key = True)
    member_id  = Column(Integer, ForeignKey('members.id'))
    interest_rate = Column(Float)
    # term in months
    current_balance = Column(Float)
    interest_accumulated = Column(Float)
    account_status = Column(String(50))
    opening_Date = Column(Date)

    def __repr__(self):
        return '<Saving: {0}, account_no: {1}'.format(self.id, self.account_no)
