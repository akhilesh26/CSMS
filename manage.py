from Models.member import Member
from Models.loan import Loan
from Models.expense import Expense

# Initialize tables
Member.create_table()
Loan.create_table()
Expense.create_table()

# Creating sample entries
# m = Member()
# m.name = "Utkarsh"
# Member.add(m)
# l = Loan()
# l.amount = 10000
# Loan.add(l)
# Loan.init(Loan)
# print(Loan.query.all())

