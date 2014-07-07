class Filter:
    def init(self):
        self.blocked=[]
    
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked=["SPAM"]
        
        
f=Filter()
f.init()
print "Parent filter is: "+str(f.filter([1,2,3]))

s=SPAMFilter()
s.init()
print "Child filter is: "+str(s.filter(["SPAM","SPAM","SPAM","SPAM","eggs","bacon"]))


