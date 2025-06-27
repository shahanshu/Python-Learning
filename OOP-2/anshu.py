''' constructor'''
#constructors are used for object initialization
class employee:
    def __init__(self,n,a,s):
        self.name=n
        self.age=a
        self.salary=s
    def info(self):
        print(f"""name: {self.name}
                age: {self.age}
                salary: {self.salary}""")
e1=employee("anshu shah",23,12000)
e1.info()

# this is called the parameterized constructur where as the previous called the default constructor 
