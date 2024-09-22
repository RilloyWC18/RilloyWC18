#getting user to input student info
studentid = (input("StudentID: "))
firstname = (input("First name: "))
lastname = (input("Last name: "))
#settup passphrase for student to enter
passphrase = (input("I am a newbie at whitecliffe college"))
#check if passphrase requirements are met and print info
if "whitecliffe" in passphrase and "college" in passphrase:
    print(studentid[0:2] + lastname[0:3])
