from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

class Database():
    def __init__(self, username='root', password='toor'):
        self.engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'\
                .format(username, password, "csms"), echo=True)
        self.Base = declarative_base()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def createTable(self):
        self.Base.metadata.create_all(self.engine)

db = Database()

# Create table
# db.createTable()

# def addMember():
    # member = Member("Utkarsh", "Papa", "Wood")
    # db.session.add(member)
    # db.session.commit()
    # print(member)


# addMember()
