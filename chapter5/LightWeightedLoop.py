#5.6
List=[x*x for x in range(10)]
print "List is: "+str(List)

List2=[x*x for x in range(10) if x%3==0]
print "List2 is: "+str(List2)

List3=[(x,y) for x in range(3) for y in range(3)]
print "List3 is: "+str(List3)