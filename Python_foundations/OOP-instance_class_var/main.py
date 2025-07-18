class Car:
    wheels=4
    noCars= 0
    companyName=" srm motors "
    def __init__(self,bName,cost,companyName):
        self.bName=bName
        self.companyName=companyName
        self.cost=cost
        # self.noCars+=1
        Car.noCars+=1
    def info(self):
        print(f"{self.bName} : {self.cost} {Car.wheels} in a toatl nof of cars {Car.noCars}")


    def amt(self):
        print(f"""the cost of: "{ self.bName}" of the company: "{self.companyName}" is "{ self.cost}" """)


car1=Car(bName="toyata",cost=24000,companyName=" Tata motors")
car2=Car("honda",34000,"land Rover")
car1.info()
car2.info()


car1.bName="rolls roys"
car1.info()
car2.info()

car2.cost=10000
car2.info()

car1.info()
car1.wheels =100
print( car1.companyName)
print(car1.wheels)
car2.amt()
car3=Car(bName=" land cruise ",companyName="landdrover",cost=4100)
car3.info()