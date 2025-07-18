try:
    a=int(input("enter a number"))
    b=int(input("enter aother  number"))
    print(f"{a} is th great ") if a>b else print(f"{b} is the greater ")
except Exception as e:
    print(f"error{e}")

    #this is only in short programs and when we needed to assign the value to the variable upon condition 

c= 45 if a == b else 45
print(c)