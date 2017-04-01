from sqlalchemy import Column, Integer, String, Date, ForeignKey
from Models.database import db
from Models.base import TableBase

class Recurring(db.Base, TableBase):
    __tablename__ = 'recurring'
    #id = Column(Integer, primary_key = True)
    account_no = Column(Integer,primary_key = True)
    member_id  = Column(Integer, ForeignKey('members.id'))
    principal_amount = Column(Integer)
    monthly_payment = Column(Integer)
    interest_rate = Column(Integer)
    # term in months
    term = Column(Integer)
    current_balance = Column(Integer)
    final_matured_amount = Column(Integer)
    interest_accumulated = Column(Integer)
    account_status = Column(String(50))
    opening_Date = Column(Date)

    def __repr__(self):
        return '<Recurring: {0}, account_no: {1}'.format(self.id, self.account_no)
