from sqlalchemy import Column, Integer, String, Date, ForeignKey
from Models.database import db
from Models.base import TableBase

class FixedDeposit(db.Base, TableBase):
    __tablename__ = 'fixedDeposit'
    #id = Column(Integer, primary_key = True)
    account_no = Column(Integer, primary_key = True)
    member_id  = Column(Integer, ForeignKey('members.id'))
    payed_amount = Column(Integer)

    interest_rate = Column(Integer)
    # term in months
    term = Column(Integer)
    final_matured_amount = Column(Integer)

    interest_accumulated = Column(Integer)
    account_status = Column(String(50))
    opening_Date = Column(Date)

    def __repr__(self):
        return '<FixedDeposit: {0}, account_no: {1}'.format(self.id, self.account_no)
