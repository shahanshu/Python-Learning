class addition:
    @staticmethod
    def sum(a,b):
        return a+b
print("the sum is ",addition.sum(4,5))

class Math:
    def __init__(self,num):
        self.num=num
    def add(self,n1):
        self.num=self.num +n1

    