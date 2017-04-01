from sqlalchemy import Column, Integer, String, Date
from Models.database import db
from Models.base import TableBase

class Member(db.Base, TableBase):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    father_name = Column(String(50))
    dob = Column(Date)
    gender = Column(String(50))
    village = Column(String(50))
    block = Column(String(50))
    district = Column(String(50))
    state = Column(String(50))
    pincode = Column(Integer)
    phone = Column(String(50))
    photo_path = Column(String(250))
    signature_image_path = Column(String(250))
    email = Column(String(50))
    id_proof = Column(String(50))
    id_number = Column(String(50))
    job = Column(String(50))
    office = Column(String(50))
    membership_type = Column(String(50))
    membership_fee = Column(Integer)
    no_of_share = Column(Integer)
    rate_at_the_time_of_buying = Column(Integer)
    payable_amount = Column(Integer)
    opening_Date = Column(Date)

    # Back refs
    # fixedAccounts = relationship('FixedDeposit', backref='member', lazy='dynamic')
    # savingAccounts = relationship('Saving', backref='member', lazy='dynamic')
    # recurringAccounts = relationship('Recurring', backref='member', lazy='dynamic')
    

    def __repr__(self):
        return '<Member: {}, {}>'.format(self.id, self.name)


# Creates the table if doesn't already exists
if __name__=="__main__":
    # Drop table if already exists
    db.createTable()


