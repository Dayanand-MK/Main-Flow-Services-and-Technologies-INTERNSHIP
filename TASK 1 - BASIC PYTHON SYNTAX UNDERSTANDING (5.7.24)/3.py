# GAIN FAMILIARITY WITH COMMON DATA STRUCTURES LIKE LIST, DICTIONARIES, AND TUPLES.

def list():
    li = [5,15,17,20,25,30]                             #list
    print("List : ",li)
    li.append(35)                                       #append
    li.insert(1,10)                                     #insert
    li.remove(17)                                       #remove
    a = li[1]                                           #index
    print("At index 1 : ",a)
    print("Updated list : ",li)

def dict():
    d = {"Name" : "Dayanand","Age" : 17,"Year" : 1}     #dictionary
    print("Dictionary : ",d)
    d["Dept"] = "AI&ML"                                 #insert
    del d["Year"]                                       #delete
    d["Age"] = 18                                       #update
    print("Updated Dictionary : ",d)

def tuple():
    t = (5,15,17,20,25,30)                              #tuple
    u = t + (35,)                                       #append
    t[:1]+t[5:]                                         #remove
    print("Removed Tuple : ",t)
    l = 10
    t[:1]+(l,)+t[6:]                                    #update
    print("Updated Tuple : ",t)

print("LIST")
list()                                                  #call function
print("DICTIONARY")
dict()                                                  #call function
print("TUPLE")
tuple()                                                 #call function
