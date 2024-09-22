
#Find items on shopping list
#items=(int(input("Number of items: ")))
#Create list of items bought and prices
#list = {input(f"Enter Item {i+1}: "): int(input(f"Enter Price {i+1}: ")) for i in range(items)}
#print("Shopping Complete: ",list)

def total(diction):
    sum=0
    for item in diction.values():
        sum+=discount(item)
    return sum
def discount ( value ) :
    if value>300 :
        disc_price = value *0.95
        print(price)

        return disc_price
    else :
        return value


dict = {}
n = int ( input ( "Number of Products : ") )
for i in range ( n ) :
    item_name = input ( " Enter name : " )
    price = int (input ( " Enter Price " ) )
    dict[item_name] = price

print(total(dict))










