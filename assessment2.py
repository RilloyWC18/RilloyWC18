
req_generator=1

#Gathering info from user
def basic_info():
    global req_generator
    date = input("enter date")
    name = input("enter name")
    staff_id = input("enter staff id")
    #
    req_id = str(req_generator + 10000)
    info_dict = {'Date': date, 'Name': name, 'Staff ID': staff_id, 'Req ID': req_id}
    return info_dict

def total_requisition():
    num = int(input("How many requisitions do you want to input"))
    total = 0
    for i in range(num):
        item_name = input("enter item")
        price = int(input("enter price"))
        total = total + price
    return total

def requisition_approval():
    total = total_requisition()
    info = basic_info()
    if total >= 500:
        status = "approved"
        approval_id = info['Staff ID'] + info['Req ID'][-3]
        info['status'] = status
        info['approval_id'] = approval_id
    return info

def display():
    req = requisition_approval()
    for k,v in req.items():
        print(k,v)

display()


