from Models.member import Member
from Models.loan import Loan
from Models.saving import Saving
from Models.deposit import Deposit
from Models.withdrawal import Withdrawal
from Models.transfer import Transfer
from Models.deposit import Deposit
from Models.database import db

# Initialize tables
db.dropTables()
Member.create_table()
Loan.create_table()
Saving.create_table()
Deposit.create_table()
Withdrawal.create_table()
Transfer.create_table()
Deposit.create_table()

# Creating sample entries
# m = Member()
# m.name = "Utkarsh"
# Member.add(m)
# l = Loan()
# l.amount = 10000
# Loan.add(l)
# Loan.init(Loan)
# print(Loan.query.all())

