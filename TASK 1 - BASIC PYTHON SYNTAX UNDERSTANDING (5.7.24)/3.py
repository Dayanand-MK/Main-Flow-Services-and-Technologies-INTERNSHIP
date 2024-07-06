# GAIN FAMILIARITY WITH COMMON DATA STRUCTURES LIKE LIST, DICTIONARIES, AND TUPLES.

def list():
    li = [5,15,17,20,25,30]
    print("List : ",li)
    li.append(35)
    li.insert(1,10)
    li.remove(17)
    a = li[1]
    print("At index 1 : ",a)
    print("Updated list : ",li)

def dict():
    d = {"Name" : "Dayanand","Age" : 17,"Year" : 1}
    print("Dictionary : ",d)
    d["Dept"] = "AI&ML"
    del d["Year"]
    d["Age"] = 18
    print("Updated Dictionary : ",d)

def tuple():
    t = (5,15,17,20,25,30)
    u = t + (35,)
    t[:1]+t[5:]
    print("Removed Tuple : ",t)
    l = 10
    t[:1]+(l,)+t[6:]
    print("Updated Tuple : ",t)

print("LIST")
list()
print("DICTIONARY")
dict()
print("TUPLE")
tuple()