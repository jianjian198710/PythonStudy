#2.3.3
#append: modify the original list
list1=[1,2,3]
list1.append(4)
print "after append: "+str(list1)

#count
list2=[[1,2],1,1,[2,1,[1,2]]]
print "count value [1,2]: "+str(list2.count([1,2]))
print "count value 1 : "+str(list2.count(1))

#extend: modify the original list
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print "a is: "+str(a)

#+: compare with extend, return a new list
a2=[1,2,3]
b2=[4,5,6]
print "a2+b2 is: "+str(a2+b2)
print "a2 is: "+str(a2)

#index
knights=["We","are","knights","who","say","ni"]
print "index 'who' is: "+str(knights.index("who"))

#insert
numbers=[1,2,3,5,6,7]
numbers.insert(3, "four")
print "numbers is: "+str(numbers)

#pop: remove the last term
x=[1,2,3]
print "x.pos() is: "+str(x.pop())
print "x is: "+str(x)

#remove: remove the first matched term
y=["to","be","or","not","to","be"]
y.remove("be")
print "y is: "+str(y)

#reverse
z=[1,2,3]
z.reverse()
print "z is: "+str(z)

#sort
list2=[4,6,2,1,7,9]
list2.sort(cmp=None, key=None, reverse=False)
print "list2 is: "+str(list2)

#copy
list3=[4,6,2,1,7,9]
#Don't use list4=list3, with using that list4 list3 point the same list object
list4=list3[:]
list4.sort(cmp=None, key=None, reverse=True)
print "list3 is: "+str(list3)
print "list4 is: "+str(list4)