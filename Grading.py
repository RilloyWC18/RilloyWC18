#Capture student marks
m1=int(input("enter m1: "))
m2=int(input("enter m2: "))
m3=int(input("enter m3: "))
m4=int(input("enter m4: "))
#Calculate avg grade
grade=(m1+m2+m3+m4)/4
#Mark final grade
if grade>50:
    print("pass")
else:
    print("not achieved")

