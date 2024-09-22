#Program to practice array manipulation

#Create an empty array called 'city'
city=[]
#Get the user to input new items to the city 5 times
for x in range(0,5):
    city.append(input("Enter city name: "))
#then, print the length of the city array
print(len(city))
#add a new city called "hong"
city.append("hong")
#Delete the first city in the list
city.pop(0)
#Reverse the city list, then print it
city.reverse()
print(city)
#Alternative method to reverse the city list
reverse_city=[]
for each_city in city[::-1]:
    reverse_city.append(each_city)
print(reverse_city)