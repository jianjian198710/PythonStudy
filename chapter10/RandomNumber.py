#10.3.6
from random import *
from time import *
date1=(2008,1,1,0,0,0,-1,-1,-1)
time1=mktime(date1)
date2=(2009,1,1,0,0,0,-1,-1,-1)
time2=mktime(date2)

random_time=uniform(time1,time2)
print asctime(localtime(random_time))

#Dices
num=input("How many dices?")
total=0
x=0
while x<num:
    #create the number between 1 and 6
    total=total+randrange(1,7)
    x=x+1
print "The result is: "+str(total)

#Card
values=range(1,11)+"Jack Queen King".split()
print "values: "+str(values)
suites="diamonds clubs hearts spades".split()
deck=["%s of %s" %(v,s) for v in values for s in suites]
print "deck[:12] is "+str(deck[:12])

shuffle(deck)
print "deck[:12] after shuffle is "+str(deck[:12])
