from sqlalchemy import Column, Integer, String, Date
from Models.database import db
from Models.base import TableBase

class Saving(db.Base, TableBase):
    __tablename__ = 'saving'
    #id = Column(Integer, primary_key = True)
    account_no = Column(Integer, primary_key = True)
    member_id  = Column(Integer, ForeignKey('members.id'))
    interest_rate = Column(Integer)
    # term in months
    current_balance = Column(Integer)
    interest_accumulated = Column(Integer)
    account_status = Column(String(50))
    opening_Date = Column(Date)

    def __repr__(self):
        return '<Saving: {0}, account_no: {1}'.format(self.id, self.account_no)