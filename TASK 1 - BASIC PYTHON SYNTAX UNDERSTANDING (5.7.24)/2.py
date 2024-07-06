# PRACTICE WRITING BASIC SCRIPTS TO PERFORM ARITHMETIC OPERATIONS, MANIPULATE STRINGS,AND USE CONDITIONAL STATEMENTS.

def arithemetic():                                                      #arithemetic operations
        a = int(input("Enter 1st number : "))                           #input
        b = int(input("Enter 2nd number : "))                           #input
        print("Addition : ",a+b)                                        #addition
        print("Subraction : ",a-b)                                      #subraction
        print("Multiplication : ",a*b)                                  #multiplication
        print("Division : ",a/b)                                        #division

def strings():                                                          #string manipulations
    s = input("Enter a String : ")                                      #input
    ss = input("Enter a string : ")                                     #input
    print("Concatenation : ",s+ss)
    print("Index of [0] : ",s[0])                                       #indexing
    print("Index of [5] : ",s[5])                                       #indexing
    print("Slicing [0:5] : ",s[0:5])                                    #slicing


#main menu based program
print("**********MENU**********")
print("1 . Arithmetic Operations\n2 . String Operations\n3 . Exit\n")
ch= int(input("Enter the choice :"))                                    #input
if ch == 1:                                                             #conditional statements
    arithemetic()                                                       #call function
elif ch == 2:
    strings()                                                           #call function
elif ch == 3:
    print("Exiting")
else:
    print("Invalid Choice !")