########## name of all validators ##########################################
#
# 1. NameWithSpaceValidator -> anything which has char or space
# 2. NameWithoutSpaceValidator -> anything which just has chararchters
# 3. NumberValidator -> anything which just has numbers -> memberId
# 4. MoneyValidator -> for money of all kinds
# 5. PincodeValidator -> for pincodes
# 6. PhoneNoValidator -> for mobile phone numbers (10 max size)
#
############################################################################





from PyQt5.QtGui import QValidator, QIntValidator
import re

LESSTHANSIXCHAR = re.compile(r'^.{,6}$')
LESSTHANTENCHAR = re.compile(r'^.{,10}$')
ALLINT = re.compile(r'^[0-9]*$')
ALLCHAR = re.compile(r'^[a-zA-Z]*$')
ALLCHARORSPACE = re.compile(r'^[a-zA-Z\s]*$')
EMPTYSTR = re.compile(r'^$')
INTORDOT = re.compile(r'^[0-9\.]*$')
MORETHANTWOPLACES = re.compile(r'.*\.[0-9]{3,}$')

RED = '#ff7f7f'
WHITE = '#ffffff'

class MyValidator(QValidator):
    def __init__(self, obj):
        super().__init__()
        self.obj = obj
        self.obj.setValidator(self)
        self.color = WHITE

class PincodeValidator(MyValidator):
    def validate(self, stri, pos):
        state = 1
        self.color = WHITE
        if EMPTYSTR.match(stri):
            self.color = RED
            print('STRING CAN\'T BE EMPTY')
        if not ALLINT.match(stri):
            self.color = RED
            print('ALL CHAR MUST BE INTEGER')
        if not LESSTHANSIXCHAR.match(stri):
            state = 0
            self.color = RED
            print('PINCODE SHOULD BE OF 6digits')
        self.obj.setStyleSheet('QLineEdit {{ background-color: {color} }}'.format(color=self.color))
        return (state, stri, pos)

class NumberValidator(MyValidator):
    def validate(self, stri, pos):
        state = 1
        self.color = WHITE
        if EMPTYSTR.match(stri):
            self.color = RED
            print('STRING CAN\'T BE EMPTY')
        if not ALLINT.match(stri):
            self.color = RED
            print('ALL CHAR MUST BE INTEGER')
        self.obj.setStyleSheet('QLineEdit {{ background-color: {color} }}'.format(color=self.color))
        return (state, stri, pos)

# CAN BE ONLY CHAR OR SPACE
class NameWithSpaceValidator(MyValidator):
    def validate(self, stri, pos):
        state = 1
        self.color = WHITE
        if EMPTYSTR.match(stri):
            self.color = RED
            print('STRING CAN\'T BE EMPTY')
        if not ALLCHARORSPACE.match(stri):
            self.color = RED
            print('ALL CHAR MUST BE INTEGER')
        self.obj.setStyleSheet('QLineEdit {{ background-color: {color} }}'.format(color=self.color))
        return (state, stri, pos)

class NameWithoutSpaceValidator(MyValidator):
    def validate(self, stri, pos):
        state = 1
        self.color = WHITE
        if EMPTYSTR.match(stri):
            self.color = RED
            print('STRING CAN\'T BE EMPTY')
        if not ALLCHAR.match(stri):
            self.color = RED
            print('ALL CHAR MUST BE INTEGER')
        self.obj.setStyleSheet('QLineEdit {{ background-color: {color} }}'.format(color=self.color))
        return (state, stri, pos)

class PhoneNoValidator(MyValidator):
    def validate(self, stri, pos):
        state = 1
        self.color = WHITE
        if EMPTYSTR.match(stri):
            self.color = RED
            print('STRING CAN\'T BE EMPTY')
        if not ALLINT.match(stri):
            self.color = RED
            print('ALL CHAR MUST BE INTEGER')
        if not LESSTHANTENCHAR.match(stri):
            self.color = RED
            print("PHONE NO MUST BE LESS THAN OR EQUAL TO 10 digits")
        self.obj.setStyleSheet('QLineEdit {{ background-color: {color} }}'.format(color=self.color))
        return (state, stri, pos)

class MoneyValidator(MyValidator):
    def validate(self, stri, pos):
        state = 1
        self.color = WHITE
        if EMPTYSTR.match(stri):
            self.color = RED
            print('STRING CAN\'T BE EMPTY')
        if not INTORDOT.match(stri):
            self.color = RED
        if MORETHANTWOPLACES.match(stri):
            state = 0
            self.color = RED
            print("TWO PLACES DECIMAL HERE")
        self.obj.setStyleSheet('QLineEdit {{ background-color: {color} }}'.format(color=self.color))
        return (state, stri, pos)

