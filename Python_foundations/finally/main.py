#finally is useful in functions where the print fails 

def test():
    try:
        lst=[2,3,4,4]
        num=int(input("enter the index to check the lsting"))
        return 1
    except Exception as e:
        print(f"error {e}")
    finally:
        ask=int(input("enter a number"))
        print(f"sqr root of{ask} is {ask*ask}")
        print(" Thanks")   
x= test()
print(x)