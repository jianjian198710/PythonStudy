#5.5.4
#zip
names=["anne","beth","george","damon"]
ages=[12,45,32,102]
print "use zip is: "+str(zip(names,ages))

#stop when the shorter is e
List=zip(range(5),xrange(10000000))
print "use zip is: "+str(List)

#sorted and reverse
print "sorted is: "+str(sorted([4,3,6,8,3]))
#reversed return a iteratable object
print "reversed is: "+str(list(reversed("Hello world!")))
print "reversed is: "+" ".join(reversed("Hello world!"))