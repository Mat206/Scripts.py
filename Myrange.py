class rnge:
    def __init__(self,min,max,step=1):
        print("__Init__")
        self.step = step
        self.max = max
        self.i = min
        self.aux = 0

    def __iter__(self):
        print("__iter__")
        return self
    
    def __next__(self):
        print("__next___")
        self.aux = self.i
        self.i += self.step
        if self.aux > self.max:
            raise StopIteration
        return self.aux 

for i in rnge(0,13):
    print(i)
        