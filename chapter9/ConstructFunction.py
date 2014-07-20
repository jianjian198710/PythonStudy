#9.2
class FooBar:
    def __init__(self):
        self.somevar=42
    
f=FooBar()
print f.somevar

#Construction with argument
class FooBar2:
    def __init__(self,value=42):
        self.somevar=value
    
f=FooBar2("This is a constructor argument!")
print f.somevar

#Super
class Bird(object):
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print "Aaaah..."
            self.hungry=False
        else:
            print "No,thanks!"

class SongBird(Bird):
    def __init__(self):
        self.sound="Squawk"
        super(SongBird,self).__init__()
    def sing(self):
        print self.sound

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()
        