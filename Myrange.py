#Script that works like range() funtion in python, created as an iterator

class rnge:
    #Init of properties in the class
    def __init__(self,min,max,step=1):
        print("__Init__")
        self.step = step
        self.max = max
        self.i = min
        self.aux = 0
       
    #Pass as an iterator
    def __iter__(self):
        print("__iter__")
        return self
    
    #Logic of process
    def __next__(self):
        print("__next___")
        self.aux = self.i
        self.i += self.step
        if self.aux > self.max:
            raise StopIteration
        return self.aux 
    
#Use example
for i in rnge(0,13):
    print(i)
        
