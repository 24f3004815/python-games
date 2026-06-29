import random as r 

comp = r.randint(0,5)
high = 0
low = 0 
eqaul = 0
try:
    user = int(input("Enter the number between 0 to 5 :"))
    
    print("Computer number is :", comp)
    while True:
        if user > 5 or user < 0:
            print("Invalid input")
            break 
        elif user > comp:
            print("Too high")
            
        elif user < comp:
            print("Too less")

        else:
            print("Equal")

except ValueError:
    print("Invalid input")
