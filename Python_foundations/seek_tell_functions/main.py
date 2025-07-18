with open('kripa.txt','r') as f:
 f.seek(5) 
 #used to move the cursor either forward or backward such 

 print(f.tell())

 #returns the current position of the cursor 
 info= f.read(40)
 print(info)

with open('kripa.txt','w') as a:
 a.write("this is the end that you've been waiting thats it is . ")
 a.truncate(10)
with open('kripa.txt','r') as a:
 info=a.read() 

 print(info)