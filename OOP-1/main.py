class person:
    name="anshu"
    age=22
    occupation="software developer"
    salary=45
    #defining an method (inside class using keyword self) 
    def anshu(self):
        print(f"name: {self.name}\n age:{self.age} \n occupation: {self.occupation} \n salary: {self.salary}")
a= person()
b=person()
c=person()
 #an instant of class
a.name="kripa"
b.name="anshu shah"
b.age=45
b.salary=456474
a.occupation="engineer"
a.occupation="farmer"
b.occupation="teacher"
a.anshu()
print("")
b.anshu()
print("")
c.anshu()
