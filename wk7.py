from datetime import date
class Ticket:
    ticket_id=1000
    ticket_statistic = []

    def __init__(self, employee_id, name, issue_desp):
        self.date = date.today()
        self.employee_id=employee_id
        self.issue_desp = issue_desp
        self.name = name
        self.ticket_id = Ticket.ticket_id
        Ticket.ticket_id += 1
        self.status = ''
        self.priority = self.assign_priority(issue_desp)
        self.resolution_message = self.resolve_password()
        Ticket.ticket_statistic.append(self)

    @staticmethod
    def create_ticket():
        name = input("Enter name: ")
        id = input("Enter ID: ")
        issue = input("What is the problem: ")
        return Ticket(name, id, issue)

    def assign_priority(self, issue_desp):

        description_lower = issue_desp.lower()
        if "system outage" == description_lower:
            return "High"
        if "password reset" == description_lower:
            return "Low"
        else:
            return "Medium"
    def resolve_password(self):
        new_password = self.employee_id[:2] + self.name[:2]
        self.resolution_message = f"Your password has been reset to: {new_password}"
        self.status = "Resolved"

    def update_status(self):


        if self.priority == "High":
            print ("The following issue needs your approval: ", self.issue_desp)
            response = input("Would you want to: Approve or Not Approve: ")
            if response == "Approve":
                self.status="Resolved"
                self.resolution_message = 'ticket approved by manager'
            if response == "Not Approve":
                self.status = "Closed"
                self.resolution_message = 'ticket not approved by manager'
        if self.priority == "Low":
            self.resolve_password()
        if self.priority == "Medium":
            self.status= "In Progress"

    @staticmethod
    def statistics():
        total_ticket = 0
        resolve = 0
        in_progress = 0
        closed = 0
        for ticket in Ticket.ticket_statistic:
            total_ticket += 1
            if ticket.status == "Resolved":
                resolve += 1
                closed += 1
            if ticket.status == "In Progress":
                in_progress += 1
            if ticket.status == "Closed":
                closed += 1
        print(".....Statistics....")
        print("The total ticker submitted is: ", total_ticket)
        print("The number of resolved ticket is: ", resolve)
        print("The number of tickets in progress is: ", in_progress)
        print("the number of closed ticket is: ", closed)

    def display(self):
        print(f"Date: {self.date}")
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee Name: {self.name}")
        print(f"Issue Description: {self.issue_desp}")
        print(f"Priority: {self.priority}")
        print(f"Status: {self.status}")
        if self.resolution_message:
            print(f"Resolution Message: {self.resolution_message}")
        print("-" * 40)

if __name__ == '__main__':
    num = int(input("How many tickets ? "))

    for i in range(num):
        tkt = Ticket.create_ticket()
        tkt.update_status()

    for ticket in Ticket.ticket_statistic:
        ticket.display()



    print("UPDATE...")
    Ticket.statistics()
