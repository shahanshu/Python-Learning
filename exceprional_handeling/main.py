try:
    num=int(input("enter number for multiplication table"))
    i=1
    for i in range(1,11):
        print(f"{num} X {i} = {num*i}")
except Exception as e:
    print(f"ERROR->{e}")
else:
    print("Multiplication Table Done ")
finally:
    print(" thanks for enter a value ")