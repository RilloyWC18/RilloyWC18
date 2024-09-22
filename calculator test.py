#Write a program to create a function calculator ()
#such that it can accept two
#variables and calculate addition and subtraction
#Also, it must return both addition and subtraction in a single return call.



def calculation(a,b):
#defining terms
    sum=a+b
    avg=a/b
    return sum,avg
#Test run code
ans=calculation(45,62)
#Printing sum only
print("The sum is ",ans[0])
#printing avg only
print("The avg is ",ans[1])
#printing both
print("The sum and avg is ",ans)

#results
#The sum is  107
#The avg is  0.7258064516129032
#The sum and avg is  (107, 0.7258064516129032)




#defining percentages
def percentage(*args):
    sum=0
#for loop to collect data
    for i in args:
        sum+=i
#calculate sum and length of parameters/list of numbers
    avg=sum/len(args)
    print('average=',avg)

#test run code
m=percentage(54,77,21,23,9,80,5)

#results
#average= 38.42857142857143




def student_grade(**kwargs):
    sum=0
    #kwargs items/keys 1st= value2nd
    for student in kwargs.items():
        print(student)
    for name in kwargs.keys():
        print(name)
    for grade in kwargs.values():
        print(grade)

#code test run

v=student_grade(IT5014=60,  IT7809=80,  IT6798=50,  IT5048=70)
print(v)

#results
#('IT5014', 60)
#('IT7809', 80)
#('IT6798', 50)
#('IT5048', 70)
#IT5014
#IT7809
#IT6798
#IT5048
#60
#80
#50
#70
#None