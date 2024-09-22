class Arithmetic:
#initializing arithmetic
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
#defining addition method
    def addition(self):
        print  (self.num1+self.num2)
 #defining subtraction method
    def subtraction(self):
        print (self.num1-self.num2)
#defining multiplication method
    def multiplication(self):
        print (self.num1*self.num2)
#defining division method
    def division(self):
        print (self.num1/self.num2)
#Code test
f1 = Arithmetic(80, 20)
f1.addition()
f1.subtraction()
f1.division()
f1.multiplication()

#Result
100
60
4.0
1600

