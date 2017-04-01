from sqlalchemy import Column, Integer, String, Date, ForeignKey
from Models.database import db
from Models.base import TableBase

class Withdrawal(db.Base, TableBase):
    __tablename__='withdrawal'
    transaction_no= Column(Integer,primary_key = True)
    from_account=Column(Integer)
    to_account=Column(Integer)
    amount=Column(Integer)
    date=Column(Integer)
    comment=Column(Integer)

    def __repr__(self):
        return '<Withdrawal: {0}, account_no: {1}'.format(self.id, self.account_no)
