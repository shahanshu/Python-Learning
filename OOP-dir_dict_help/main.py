class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

anshu=person(name="anhsu ",age=67)
print(anshu.__dict__)


a="hey there i'm a string"
print(dir(a))  # this a functions


print(help(anshu))