

#Gathering number of students


stu_num=(int(input("Number of students: ")))

#ALTERNATIVE METHOD
#student=(input("Enter Student Name: "))
#reg=(input("Enter Student Registration: "))
#list[reg]=student

#Gathering student name and registration from user

list = {input(f"Enter Student Name {i+1}: "): input(f"Enter Student Registration {i+1}: ") for i in range(stu_num)}

print("Dictionary Complete: ",list)
#Test code run

#W100’: ‘Paul’, ‘W101’: ‘Emma’, ‘W102’: ‘John’

##result
#Enter Student Name 2: Emma
#Enter Student Registration 2: W101
#Enter Student Name 3: John
#Enter Student Registration 3: W102
#Dictionary Complete:  {'Paul': 'W100', 'Emma': 'W101', 'John': 'W102'}

