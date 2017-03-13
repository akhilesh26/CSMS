from sqlalchemy import Column, Integer, String, Date, ForeignKey
from Models.database import db
from Models.base import TableBase

class Transfer(db.Base, TableBase):
    __tablename__='transfer'
    transaction_no= Column(Integer,primary_key = True)
    account_no = Column(Integer,ForeignKey('members.id'))
    member_id=Column(Integer)
    amount=Column(Integer)
    date=Column(Integer)
    comment=Column(Integer)

    def __repr__(self):
        return '<Deposit: {0}, account_no: {1}'.format(self.transaction_no, self.account_no)
