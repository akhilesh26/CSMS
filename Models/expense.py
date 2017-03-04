from sqlalchemy import Column, Integer, String, Date
from Models.database import db
from Models.base import TableBase

class Expense(db.Base, TableBase):
    __tablename__ = "expense"
    id = Column(Integer, primary_key=True)
    type = Column(String(50))
    cost = Column(String(50))
    payment_method = Column(String(50))
    date = Column(Date)

    def __repr__(self):
        return '<Expense: {}, {}>'.format(self.id, self.type)


# Creates the table if doesn't already exists
if __name__=="__main__":
    # Drop table if already exists
    db.createTable()