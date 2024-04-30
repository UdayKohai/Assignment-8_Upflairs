try:
    
    lst1=[]
    n= int(input("Enter no of elements in the list  : "))
    for i in range(0,n,1):
        element =str(input(f"Enter element {i+1} :"))
        lst1.append(element)

    print(lst1)
    word = lst1[0]
    for item in lst1:
        m=len(word)
        if m<len(item):
            word=item
        elif m==len(item):
            word = word
        else:
            continue

    print(f"Longest word = {word}")

except IndexError:
    print("Enter a valid number for elements of list")
