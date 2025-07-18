"""super.__init__( parameters) are used to call parent class constructors """


class teachers:
  def __init__(self,name,age):
   self.name=name
   self.age=age

class students(teachers):
  def __init__(self,name,age,rollNo):
    super().__init__(name,age)
    self.rollNo=rollNo

s1=students("jerrysam",7,8)
print(f"name of student: {s1.name} age:{s1.age} roll number is : {s1.rollNo}")