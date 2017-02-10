class Member():
    def __init__(self, name, age):
        self.attribute = {}
        self.name = name
        self.age = age

    def set(self,key,value):
        self.attribute[key] = value
    
    def get(self,key):
        return self.attribute.get(key,None)
        # return self.attribute[key]
    
    def getInfo(self):
        return self.attribute

    def print(self):
        for k,v in self.attribute.items():
            print(k,v)

    def save(self):
        from database import Database
        db.run_query('insert into member values ({},{},{},{},{},{},{}).format(self.name, self.age, self.fathername)'



