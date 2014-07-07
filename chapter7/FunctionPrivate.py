class Secretive:
    #private function start with __
    def __inaccessible(self):
        print "Bet you can't see me!"
    
    def accessible(self):
        print "The secret message is:"
        #can access private function when in the class
        self.__inaccessible()
        
s=Secretive()
s.accessible()