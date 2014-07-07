#5.5
#while
x=1
while x<=100:
    print str(x)
    x=x+1
    
#for
words=["This","is","an","ex","parrot"]
for word in words:
    print word

#range
for number in range(1,101):
    print number
    
#key,value
d={"x":1,"y":2,"z":3}
for key,value in d.items():
    print "key="+key+" value="+str(value)    