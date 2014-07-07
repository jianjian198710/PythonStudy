#5.5.5
#break
from math import sqrt
for n in range(99,81,-1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
else:
    print "Don't find it"

#while true
while True:
    word = raw_input("Enter a word: ")
    if not word: break
    print "The word is: "+word