
# a function for a calulator adding and subtrating

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y


while True: 
    input1=int(input("Enter the first number:"))

    input2=int(input("Enter the second number:"))

    print("Do you want to add or subtract")

    add_sub= input("Enter add or subtract:")
    if add_sub == "add":
        print("The sum of the two numbers is:",add(input1,input2))
    if add_sub == "sub":
        print("The difference of the two numbers is:",subtract(input1,input2))
   
    print("Do you want to continue? (y/n)")
    if input("Enter y or n:") == "n":
        break
    
