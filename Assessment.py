def staff_info():

    date = str(input("Enter date:  "))
    req = int(input("Enter Requisition ID:  "))
    staff_id = input("Enter Staff ID:  ")
    name = input("Enter Full name:  ")
    return (date,req,staff_id,name)

k = staff_info()


def requisitions_total():
    dict={}
    sum=0
    n = int(input("Number of Requisition Items : "))
    for i in range(n):
        item_name = input(" Enter Item name :  ")
        price = int(input(" Enter Item Price :  "))
        sum = sum+price
    return dict{item_name,  sum}


   # print(dict+price))

a = requisitions_total()
print(k,a)

def req_approval():
    status = "pending..."



    #items=0
    #items = {input(f"Enter Requisition Item: ")}
    #prices = int(input(f"Enter Price: "))
    #sum(prices)
      #  return ("Requisition Total:  ",dict(prices))
#a=requisitions_total()
#print(a)
