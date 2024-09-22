#Write a function to sum all the numbers from an array.
# Your program should allow the user to determine the length of the array.
array = [1, 2, 3, 4, 5]
total = sum(array)
print(total)

####Result#####
#15

#Write a program to create a function calculator () such that it can accept two variables and calculate addition and subtraction.
# Also, it must return both addition and subtraction in a single return call.
#defining terms
def calculation(a,b):
    sum=a+b
    avg=a/b
    return sum,avg
#codetest run
ans=calculation(75,5)
#printing the sum only
print("The sum is ",ans[0])
#printing the avg only
print("/The avg is ",ans[1])
#printing full answer
print("The sum and avg is ",ans)
#####Result#####
#The sum is  80
#/The avg is  15.0
#The sum and avg is  (80, 15.0)

def percentage(*args):
    sum=0
    #get total
    for i in args:
        sum+=i
#calculate average
    avg=sum/len(args)
    print("Average - ",avg)
#codetest run
percentage(32,55,78,20)

#####result#####
#Average -  46.25

#Define function
def student_grades(**kwargs):
    sum=0
    for i in kwargs.values():
        sum+=i
    return sum
    for i in kwargs.keys():
        sum+=i
    return sum

k = student_grades(Simon=98,Max=100,Taran=50,Rilloy=85)
print(k)

res=student_grades(IT5014=60,  IT7809=80,  IT6798=10)