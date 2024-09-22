class RequisitionSystem:
    #INITIALIZING REQUISITION ID AND SUM OF PRICES
    req_requests = 0
    req_approved = 0
    req_not = 0
    req_pending = 0
    requisition_id = 1000
    sum = 0
    #INITIALIZING CLASS
    def __init__(self,date,staff_id,name,status):
        date = self.date
        staff_id = self.staff_id
        name = self.name
        status = self.status
    def staff_info(self,date,staff_id,name,status):
        date = input("Enter Date")
        staff_id = input("Enter Staff ID")
        name = input("Enter Name")
        status = "Pending"
        return ticket(date,staff_id,name,status)
    def requisition_details(self):
        dict = {}
        n = int(input("Number of Requisition : "))
        for i in range(n):
            item_name = input(" Enter Item name :  ")
            price = int(input(" Enter Item Price :  "))
            sum += price
            dict[item_name] = price
            req_request += 1
        return sum
    def requisition_approval(self):
        if sum >= 500:
            self.status = "Approved"
            ref_num += str( ['staff_id'] + ['requisition_id'] [-3:])
            req_approved += 1
            return status,ref_num
        else:
            self.status = "Pending"
            req_pending += 1
            return status
    def respond_requisition(self):
        if self.status == "Pending":
            v = input("Do you approve request? Y/N")
            if v == "Y":
                status = "Approved"
                req_approved += 1
                return status
            if v == "N":
                status = "Not Approved"
                req_not += 1
                return status
            else:
                return status
    def display_requistions(self):
        Print("Requisition Items ",RequisitionSystem.sum)
    @staticmethod
    def requisition_statistics():
        print("Total Requisitions Submitted",req_requests)
        print("Total Requisitions Approved",req_approved)
        print("Total Requisitions Not Approved",req_not)
        print("Total Requisitions Pending", req_pending)

RequisitionSystem()






