#3.4
#find
title="Monty Python's Flying Circus"
print str(title.find("Monty"))
print str(title.find("Python"))
print str(title.find("Zirquess"))

subject="$$$ Get rich now!!! $$$"
#find from index1
print "find from index1: "+str(subject.find("$$$",1))
#find between index0 to 15
print "find between index0 to 15: "+str(subject.find("!!!",0,16))

#join: function reverse to spilt
seq=["1","2","3","4","5"]
sep="+"
print "sep.joint(seq) is: "+str(sep.join(seq))

#split:
seq2="1+2+3+4+5"
print "seq2.spilt('+') is: "+str(seq2.split("+"))

#lower
string="What a fucking day!"
print "lower is: "+str(string.lower())

#replace
string2="This is a test"
print "replace is: "+string2.replace("is", "ezz")

#strip: remove the space at both sides of string
names=["gumby","smith","jones"]
name="gumby "
if name.strip() in names: print "found it!"

string3="**SPAM*for*everyone!!! ***"
print "string3.strip(' *!') is: "+string3.strip(" *!")