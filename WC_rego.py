
membership_stat=[]
#INITIALIZING MEMBERSHIP CLASS
class Membership:
    status = "Active"
    counter = 1000
    all_membership = []
    def __init__(self):
        self.name = ''
        self.stu_id=''
        self.programme = ''
        self.membership_id = ''
        self.status = Membership.status
        #MAKING A LIST FOR ALL INFO INPUTED BY USER
        Membership.all_membership.append(self)
#GIVING MEMBERSHIP ID NUMBER
    def gen_membership_id(self):
        Membership.counter +=1
        return Membership.counter
#USER ENTRY AND INFO INPUT
    def data_entry(self):
        self.name = input("Enter name: ")
        self.stu_id = input("Enter student ID:  ")
        self.programme = input("Enter programme:  ")
        self.membership_id = self.gen_membership_id()
#METHOD TO DISPLAY ALL VALID INFO
    def display(self):
        print("Membership ID: ", self.membership_id)
        print("Name: ", self.name)
        print("programme: ", self.programme)
        print("Status: ", self.status)

    def withdraw(self,name):
        if self.name == name:
            self.status = "Withdrawn"
#DISPLAYING STATISTICS
    def statistics():
        active = 0
        withdrawn = 0
        diploma = 0
        bachelor = 0
        for a_membership in Membership.all_membership:
            if a_membership == "active":
                active += 1
            if a_membership == "withdrawn":
                withdrawn += 1
            if a_membership.programme == "diploma":
                diploma += 1
            if a_membership.programme == "bachelor":
                bachelor += 1
        print("Statistics:  ")
        print("Active members: ",active)
        print("Students Withdrawn", withdrawn)
        print("Diploma students: ", diploma)
        print("Bachelor students: ", bachelor)

if __name__ == '__main__':
    num = int(input("How many students would you like to register: "))

    for i in range(num):
        mem = Membership()
        mem.data_entry()

    for member in Membership.all_membership:
        member.display()
    for member in Membership.all_membership:
        member.withdraw("loy")
        member.display()
    Membership.statistics()

