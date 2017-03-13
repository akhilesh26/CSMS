from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from Models.database import db
from Models.base import TableBase

class Recurring(db.Base, TableBase):
    __tablename__ = 'recurring'
    #id = Column(Integer, primary_key = True)
    account_no = Column(String(10), primary_key = True)
    member_id  = Column(Integer, ForeignKey('members.id'))
    monthly_payment = Column(Float)
    interest_rate = Column(Float)
    # term in months
    term = Column(Integer)
    duration = Column(Integer)
    current_balance = Column(Float)
    final_matured_amount = Column(Float)
    interest_accumulated = Column(Float)
    account_status = Column(String(50))
    opening_Date = Column(Date)

    def __repr__(self):
        return '<Recurring: {0}, account_no: {1}'.format(self.member_id, self.account_no)
