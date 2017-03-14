########## name of all validators ##########################################
#
# 1. NameWithSpaceValidator -> anything which has char or space
# 2. NameWithoutSpaceValidator -> anything which just has chararchters
# 3. NumberValidator -> anything which just has numbers -> memberId
# 4. MoneyValidator -> for money of all kinds
# 5. Pincode -> for pincodes
# 6. PhoneNoValidator -> for mobile phone numbers (10 max size)
#
############################################################################





from PyQt5.QtGui import QValidator, QIntValidator
import re

LESSTHANSIXCHAR = re.compile(r'^.{,5}$')
MORETHANSIXCHAR = re.compile(r'^.{7,}$')
LESSTHANTENCHAR = re.compile(r'^.{,9}$')
MORETHANTENCHAR = re.compile(r'^.{11,}$')
ALLINT = re.compile(r'^[0-9]*$')
ALLCHAR = re.compile(r'^[a-zA-Z]*$')
ALLCHARORSPACE = re.compile(r'^[a-zA-Z\s]*$')
EMPTYSTR = re.compile(r'^$')
INTORDOT = re.compile(r'^[0-9\.]*$')
MORETHANTWOPLACES = re.compile(r'.*\.[0-9]{3,}$')

RED = '#ff7f7f'
WHITE = '#ffffff'

def setBackgroundColor(obj, color):
    obj.setStyleSheet('QLineEdit {{ background-color: {color} }}'.format(color=color))
   
class MyValidator(QValidator):
    def __init__(self, obj):
        super().__init__()
        self.obj = obj
        self.obj.setValidator(self)
        self.color = WHITE
        self.state = 1
class InRange(MyValidator):
    def __init__(self,obj,min,max):
        super().__init__(obj)
        self.min=min
        self.max=max
    def validate(self, stri, pos):
        self.state = 2
        self.color = WHITE
        if EMPTYSTR.match(stri):
            self.state = 1
            self.color = RED
        elif not ALLINT.match(stri):
            self.state = 1
            self.color = RED
        else:
            val=float(stri)
            if self.min>val or val>self.max:
                self.state=1
                self.color=RED
        setBackgroundColor(self.obj, self.color)
        return (self.state, stri, pos)


class Required(MyValidator):
    def validate(self, stri, pos):
        self.state = 2
        self.color = WHITE
        if EMPTYSTR.match(stri):
            self.state = 1
            self.color = RED
        setBackgroundColor(self.obj, self.color)
        return (self.state, stri, pos)

class Pincode(MyValidator):
    def validate(self, stri, pos):
        self.state = 2
        self.color = WHITE
        if LESSTHANSIXCHAR.match(stri):
            self.state = 1
            self.color = RED
        if EMPTYSTR.match(stri) or not ALLINT.match(stri):
            self.state = 1
            self.color = RED
        if MORETHANSIXCHAR.match(stri):
            self.state = 0
        setBackgroundColor(self.obj, self.color)
        return (self.state, stri, pos)

class Number(MyValidator):
    def validate(self, stri, pos):
        self.state = 2
        self.color = WHITE
        if EMPTYSTR.match(stri):
            self.state = 1
            self.color = RED
        if not ALLINT.match(stri):
            self.state = 1
            self.color = RED
        setBackgroundColor(self.obj, self.color)
        return (self.state, stri, pos)

# CAN BE ONLY CHAR OR SPACE
class String(MyValidator):
    def validate(self, stri, pos):
        self.state = 2
        self.color = WHITE
        if EMPTYSTR.match(stri):
            self.state = 1
            self.color = RED
        if not ALLCHARORSPACE.match(stri):
            self.state = 1
            self.color = RED
        setBackgroundColor(self.obj, self.color)
        return (self.state, stri, pos)

class Word(MyValidator):
    def validate(self, stri, pos):
        self.state = 2
        self.color = WHITE
        if EMPTYSTR.match(stri):
            self.state = 1
            self.color = RED
        if not ALLCHAR.match(stri):
            self.state = 1
            self.color = RED
        setBackgroundColor(self.obj, self.color)
        return (self.state, stri, pos)

class MobileNo(MyValidator):
    def validate(self, stri, pos):
        self.state = 2
        self.color = WHITE
        if LESSTHANTENCHAR.match(stri):
            self.state = 1
            self.color = RED
        if EMPTYSTR.match(stri) or not ALLINT.match(stri):
            self.state = 1
            self.color = RED
        if MORETHANTENCHAR.match(stri):
            self.state = 0
        setBackgroundColor(self.obj, self.color)
        return (self.state, stri, pos)

class Money(MyValidator):
    def validate(self, stri, pos):
        self.state = 2
        self.color = WHITE
        if EMPTYSTR.match(stri):
            self.state = 1
            self.color = RED
        if not INTORDOT.match(stri):
            self.state = 1
            self.color = RED
        if MORETHANTWOPLACES.match(stri):
            self.state = 0
            self.color = RED
        setBackgroundColor(self.obj, self.color)
        return (self.state, stri, pos)

class Validator:
    def __init__(self, arr):
        self.arr = arr
        self.arr.reverse()
        self.valid = False

    def is_valid(self):
        self.valid = True
        for item in self.arr:
            if item.state != 2:
                self.valid = False
                item.obj.setFocus()
                print(item)
                # setBackgroundColor(item.obj,RED)
        return self.valid

    def append(self, item):
        self.arr.append(item)
        

