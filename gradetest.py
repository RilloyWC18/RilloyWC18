def marks():
    score=[]
    no_entry=int(input("How many marks would you like to enter:  "))
    for i in range(no_entry):
        grade=int(input("Enter mark "+ str(i+1)+": "))
        #grade = int(input("Enter mark: "))
        score.append(grade)
    return score
def add(list1):
    sum = 0
    for x in list1:
        sum = x + sum
    return sum
def avg(list1):
    sum=add(list1)
    return sum/len(list1)
#print(marks())
def main():
    entry=marks()
    average=avg(entry)
    if average<50:
        print("Failed...")
    else:
        print("Pass")

main()