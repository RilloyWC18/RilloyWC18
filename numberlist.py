list1 = [10,20,30,40]

def add(list1):
    sum = 0
    for x in list1:
        sum = x + sum
    return sum
def avg(list1):
    sum=add(list1)
    return sum/len(list1)
print(add(list1))
print(avg(list1))