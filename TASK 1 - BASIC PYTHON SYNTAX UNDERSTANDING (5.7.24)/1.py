# STUDY PYTHON SYNTAX THROUGH TUTORIALS AND SIMPLE CODING EXERCISES

name = "Python for programmers"                          #string with double quote
price = 725.05                                           #float
qty = 3                                                  #integer
available = True                                         #boolean
author = 'deitel'                                        #string with single quote
ite = 2                                                  #integer

def auth():                                              #user-defined function
    if available:                                        #conditional statement
        print(f"{author} wrote this book")
    else:
        print(f"{author} does not wrote this book")

for j in range(ite):                                     #looping statement
    if qty <= 0:                                         #conditional statement
        print("Available")
    else:
        print("Not available")

    for i in range(qty-1):                               #looping statement
        print("qty = ",i)
        auth()                                           #call function
    print("Executed")