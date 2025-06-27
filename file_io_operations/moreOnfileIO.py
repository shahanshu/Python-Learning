with open('anshu.txt','r') as f:
    while True:
        line=f.readline()
        if not line:
            break
        print(line)


'''
readlines and the write lines are left for the later learning 
 for now let's focus on the basics of the file i/o
'''