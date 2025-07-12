class books:
    def __init__(self):
        self.name=['anshu','kripa','junu']
    

    def __len__(self):
        return len(self.name)

b1=books()
print(len(b1))