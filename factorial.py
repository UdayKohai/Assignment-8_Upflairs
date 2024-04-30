try:
    
    n = int(input("Enter a Number : "))
    f=1
    if n>=0:
        for i in range(1,n+1,1):
            f*=i
        print("Factorial of ",n,' : ',f)
    else:
        raise ValueError("Negative Number Entred.")

except Exception as e:
    print(f"Error : {e}")