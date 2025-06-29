"""
Getters and setters are the methods used in the oop to control access to the an onject's attribute - enforcing " encapsulation "

> also helps classes safer and moremaintainable

> Rule: Getters/Setters Must Match the Property Name
"""
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @property
    def age(self):
        return self.age
    @age.setter
    def age(self,new_age):
        if new_age<0:
            print("Invalid age")
        self._age= new_age 
anshu=person(name="anshu shah",age=22)

# self.age = property name 
#self._age = actual varibles storing the data 

            