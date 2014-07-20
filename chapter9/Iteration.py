#9.6
class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    #implement __iter__
    def __iter__(self):
        return self
    #implement next
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a

fibs=Fibs()
for f in fibs:
    if f>1000:
        print f
        break
    
    
class TestIterator:
    value=0
    def __iter__(self):
        return self
    def next(self):
        self.value=self.value+1
        if self.value>10:
            raise StopIteration
        return self.value
    
Ti=TestIterator()
print list(Ti)