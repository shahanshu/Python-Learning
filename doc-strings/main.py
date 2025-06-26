def square(n):
    '''
    takes aan input and then prrint the squrre of the number''' #his is no a comments rather a string that the python gives more preference also a helpful when we needed info  what is being fed to the function 

    print(n*n)
print(square.__doc__) #def_name.__doc__
square(5)

def studentName(name):
    print("testing")
    '''
    this takes the name of students'''
    if name=="anshu":
        print(f"role:Admin",f"name: {name}")
    else:
        print(f"role: student\n",f"name: {name}")


takeStudentName=input("enter you name: ")
studentName(takeStudentName)
print(studentName.__doc__)

#doc-string should be right below the function definition otherwise it will be ignored otherwise this will be displayed as "none"
