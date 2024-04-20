print("Welcome to Ben's Expense Tracker")


print("1. Add Expense")
print("2. Remove Expense")
print("3. Exit")


choose=input("Choose between (1)(2)(3):")


def add(x,y):
   return x+y
def sub(x,y):
   return x-y


num1= float(input("What are your current expenses? :"))
num2= float(input("How much is the expense you need to add or remove? :"))


if (choose=='1'):
   print(add(num1, num2))
   print("Is the new balance.")

elif (choose=='2'):
   print(sub(num1,num2), "Is the new balance.")
   
elif(choose=='3'):
   print("Goodbye")
#    exit() will not work here
# break will not either because it is not a loop