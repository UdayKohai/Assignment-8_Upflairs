
def MAX(lst):
    m=lst[0]
    for item in lst:
        if m<=item:
            m= item
        else:
            pass
            
    print(f"Max = {m}")
    return m

def MIN(lst):
    m= lst[0]
    for item in lst:
        if m>=item:
            m= item
        else:
            pass
    print(f"MIN = {m}")
    return m
try:
    
    lst1=[]
    n= int(input("Enter no of elements in the list  : "))
    for i in range(0,n,1):
        element =int(input(f"Enter element {i+1} :"))
        lst1.append(element)
        
    print("List : ",lst1)
    MIN(lst1)
    MAX(lst1)
    
except IndexError:
    print("Invalid size for a list.")    
except TypeError:
    print("Enter a valid Element.")