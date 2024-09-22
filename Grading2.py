score=int(input("enter your score: "))
while (score <= 0 or score >= 100):
    score = int(input("enter your score: "))
if (score >= 80):
     print("A")
elif (score >= 60):
    print("B")
elif (score >= 50):
    print("C")
else:
    print("F")