def summation(*args):
    #set container to empty
    sum=0
    for i in args:
        #putting numbers into equation
        sum+=i
    return sum
v=summation(98,34,54,23,76,45,3,5,999,6)
print(v)

def percentage(*args):
    sum=0
    for i in args:
        sum+=i
        #calculate sum and length of parameters/list of numbers
    avg=sum/len(args)
    print('average=',avg)

percentage(54,72,9)


def student_grade(**kwargs):
    sum=0
    #kwargs items/keys 1st= value2nd
    for student in kwargs.items():
        print(student)
    for name in kwargs.keys():
        print(name)
    for grade in kwargs.values():
        print(grade)



v=student_grade(Rilloy=85,Max=98,Taran=90,Simon=50)
print(v)


# Search how to use a random method to generate random numbers.
# Write a Python function that will generate random numbers from 1-20 without repetition.
# Program to generate a random number between 0 and 9
# importing the random module
import random
print(random.randint(0,20))
#This returns a number N in the inclusive range [a,b]
#meaning a <= N <= b, where the endpoints are included in the range.
