
'''
Only the methods that are defined inside the class can be used onto the rep. object 

class property -> class2 property  
'''
class employee:
    def __init__(self,name,id):
        self.name=name
        self.id= id
    def info(self):
        print(f"employeee name : { self.name}\n  elmpoyeeId : { self.id}")

class programmer(employee):
    def lang(self):
        print("python language used")
        print(f"name : {self.name }")

e1= employee(name="Divya",id= 440)
e2= programmer(name="Smirti",id= 400)
e3= employee(name="Kripa",id= 450)
e1.info() 
e2.lang()# this will thorw an error cause initally the e2 is not defined with the language so that we needed to fix the class first 
e3.info()