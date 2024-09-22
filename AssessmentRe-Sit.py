#Initializing counter
counter = 1

#Defining customer info intake from user
def customer_booking():
    name = input("Enter name here: ")
    passenger_id = input("Enter Passenger ID here: ")
    return (name,passenger_id)

#Generating ticket id number
def generate_ticket_id():
    global counter
    ticket_id = counter + 20000
    counter += 1  # Increment the counter for the next ID
    return ticket_id


#Calculating total cost of service on ferry
def service_total():
    dict = {}
    sum = 0
    n = int(input("Number of Services used on ferry : "))
    for i in range(n):
        item_name = input(" Enter Item name :  ")
        price = int(input(" Enter Item Price :  "))
        sum+=price
        dict [ item_name ] = price
    return("Total price for Items", sum)

#k = customer_booking()
#l = generate_ticket_id()
#m = service_total()

#print(k,l)
#print(m)

#ALLOWING MANAGER TO DECIDE APPROVAL OR NOT
def booking_approval():
    status = ("pending...")
    v, g = customer_booking()
    w = service_total()
    o = generate_ticket_id()
    a = input("Would you like to approve this booking?Y/N")
    if "Y" in a:
        status = "approved"
        approval_ref = v[:3]+str(o)[:-2]
        print( "Status for booking: ", status, approval_ref)

    else:
        status = "pending..."
        approval_ref = "none"
        print(status)

   