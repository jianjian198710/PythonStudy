numbers=[1,2,3,4,5,6,7,8,9,10]
print numbers[7:10]

#wrong, output is []
print numbers[-3:0]
#right
print numbers[-3:]

#The third number is step
print numbers[0:10:2]

#when the third number <0 , iteration from right to left
print "The third number<0"
print numbers[5::-2]
print numbers[:5:-2]

#number*Serial
print 5*'python'