#2.3.2
#delete term
names=["Alice","Beth","Cevil"]
del names[1]
print "After delete: "+str(names)

#setting value with patch
name=list("Perl")
print "After list: "+str(name)
name[1:]=list("ython")
print "After patch setting value: "+str(name)

#insert with patch
numbers=[1,5]
numbers[1:1]=[2,3,4]
print "After patch numbers is: "+str(numbers)

#delete with patch
numbers[1:4]=[]
print "Restore numbers: "+str(numbers)