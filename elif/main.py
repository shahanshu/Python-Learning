cart=int(input("enter the kg you want to buy"))
price= 120
print(" the price of the mango is ","Rs",price)
if(cart*price>500):
 print("price exceed rs 500")
elif(cart*price <500 and cart*price >0):
    print("Total Price is under the budget")
elif cart*price== 0:
   print("you have get an discount 100%")
else:
   print("transaction failed ..Try again ")
print("thanks for shopping")