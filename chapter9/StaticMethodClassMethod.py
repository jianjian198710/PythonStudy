#9.5.2
class MyClass(object):
    @staticmethod
    def smeth():
        print "This is a static method"
        
    @classmethod
    def cmeth(cls):
        print "This is a class method",cls
        
MyClass.smeth()
MyClass.cmeth()