class Cars:
    #initializing cars class
    def __init__(self,name, speed,mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

#defining car name method
    def car_name(self):
        print ("Car is " + self.name)
#defining car mileage method
    def car_mileage(self):
        print (self.mileage*10)

f1 = Cars("Mercedes", 100, 12000)
f1.car_name()
f1.car_mileage()

#Code result
#Car is Mercedes
#120000