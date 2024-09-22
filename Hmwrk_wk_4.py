# Global variable for the counter
counter = 1

def generate_insurer_id():
    global counter
    insurer_id = counter + 100
    counter += 1  # Increment the counter for the next ID
    return insurer_id

def collect_insurance_claim_info():
    # Collecting inputs
    date = input("Enter the date of the claim (DD-MM-YYYY): ")
    name = input("Enter the name of the insurer member: ")

    # Generating a unique insurer ID
    insurer_id = generate_insurer_id()

    # Creating a dictionary to return the information
    claim_info = {
        "Date": date,
        "Name": name,
        "Insurer ID": insurer_id,
    }

    return claim_info

def collect_claim_items():
    claim_details = {}
    total_value = 0

    # Ask user how many claims they will make
    num_claims = int(input("How many claims will you make? "))

    for i in range(num_claims):
        claim_name = input("Enter the name of the claim item: ")
        claim_price = float(input(f"Enter the price for {claim_name}: "))
        claim_details [claim_name] = claim_price
        total_value += claim_price

    return total_value


def claim_approval():
    status = "pending..."
    #approved_id = None
    info = collect_insurance_claim_info()
    total = collect_claim_items()
    if total < 1000 :
        status = "approved..."
        approved_id = str(info ['Insurer ID']) + info ['Name'] [-3:]
    else:
        status = "pending..."
        approved_id = None
    for k , v in info.items():
        print (k,v)
    print (total)
    print (status)
    print (approved_id)
    if status == 'pending...':
        k=change_status(status)
        print (k)


#if  __name__ ==  "__main__":
    #claim_approval ()




def change_status(status):

    k=input("Do you approve changing status to Approved ? type 'yes' if so:  ")
    if k== "yes":
        status='Approved...'
    return status

claim_approval()