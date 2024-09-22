class Ticket:
    ticket_id = 1000
    ticket_statistics = []

    def __init__(self, sub_date, employee_id, name, issue_desp, new_password):
        self.sub_date = sub_date
        self.employee_id = employee_id
        self.name = name
        self.issue_desp = issue_desp
        self.ticket_id = Ticket.ticket_id
        Ticket.ticket_id += 1
        self.status = 'In Progress'
        self.priority = self.assign_priority(issue_desp)
        self.resolution_message = f"Your new password is: {new_password}"
        Ticket.ticket_statistics.append(self)


    @staticmethod
    def create_ticket():
        date = input("Enter the date: ")
        name = input("Enter the name: ")
        id = input("Enter the ID: ")
        issue = input("What is your problem?: ")
        return Ticket(date,id,name,issue)

    def assign_priority(self, issue_desp):
        issue_desp = self.issue_desp
        descripton_lower = issue_desp.lower()
        if "system outage" == descripton_lower:
            return 'High'
        if "password reset" == descripton_lower:
            return 'Low'
        else:
            return 'Medium'

    def resolve_password(self):
        new_password = self.employee_id[:2] + self.name[:2]
        self.resolution_message = f"Your new password is: {new_password}"
        self.status = "Resolved"

    def manager_approval(self):

        if self.priority == 'High':
            approv = input("Approve or Not Approve: ")
            if approv == "Approve":
                self.status = "Resolved"
                self.resolution_message = "Ticket approved by Manager"
            if approv == 'Not Approve':
                self.status = "Closed"
                self.resolution_message = "Ticket not approved by Manager"
        else:
            self.status = "In Progress"

    @staticmethod
    def statistics():
        total_ticket = 0
        resolve = 0
        in_progress = 0
        closed = 0
        for ticket in Ticket.ticket_statistics:
            total_ticket +=1
            if ticket.status == "Resolved":
                resolve += 1
                closed += 1
            if ticket.status == "In Progress":
                in_progress += 1
            if ticket.status == "Closed":
                closed += 1

    def display(self):
        print(f"Date: {self.date}")
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Issue_description: {self.issue_desp}")
        print(f"Priority: {self.priority}")

if __name__ == '__main__':
    num = int(input("How many Tickets"))

    for i in range(num):
        tkt = Ticket.create_ticket()
    for ticket in Ticket.ticket_statistics:
        Ticket.display()

    Ticket.statistics()
    Ticket.update_status()
    print("Update")
    










