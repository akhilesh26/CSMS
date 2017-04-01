from sqlalchemy import Column, Integer, String, Date, ForeignKey
from Models.database import db
from Models.base import TableBase

class Loan(db.Base, TableBase):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key = True)
    account_no = Column(Integer)
    member_id  = Column(Integer, ForeignKey('members.id'))
    principal_amount = Column(Integer)
    loan_type = Column(String(50))
    # term in months
    term = Column(Integer)
    monthly_payment = Column(Integer)
    interest_rate = Column(Integer)
    total_payable_amount = Column(Integer)
    account_status = Column(String(50))
    payed_amount = Column(String(50))
    opening_Date = Column(Date)

    def __repr__(self):
        return '<Loan: {0}, type: {1}'.format(id, type)
