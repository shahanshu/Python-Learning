'''
# 
with open('file_io_operations/anshu.txt', 'r') as f:
    content = f.read()
    print(content)

# No need to write f.close()!
with open('file_io_operations/oggy.txt') as f:
    content=f.read()
    print(content)
'''
'''
with open('file_io_operations/anshu.txt','rt') as f:
    info=f.read()
    print(f"the content is {info}")
    print(type(info))
'''
#writting to the file

with open('kripa.txt','w') as f:
    f.write("this is the end ! hope fully sdfs")
