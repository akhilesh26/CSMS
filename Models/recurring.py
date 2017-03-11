from sqlalchemy import Column, Integer, String, Date
from Models.database import db
from Models.base import TableBase

class Recurring(db.Base, TableBase):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key = True)
    account_no = Column(Integer)
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
        return '<Loan: {0}, type: {1}'.format(id, type)
