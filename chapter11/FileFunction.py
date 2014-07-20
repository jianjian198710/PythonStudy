#11.2.5
f=open("H:\Developer\Java work space\PythonStudy\chapter11\somefile.txt")
print "f.read(7) is: "+f.read(7)
print "f.read(4) is: "+f.read(4)
f.close()

f2=open("H:\Developer\Java work space\PythonStudy\chapter11\somefile.txt")
print "f2.read() is: "+f2.read()
f2.close()

f3=open("H:\Developer\Java work space\PythonStudy\chapter11\somefile.txt")
for i in range(2):
    print str(i)+": "+f3.readline(),
print str(3)+": "+f3.readline()
f3.close()

import pprint
print "\n"
pprint.pprint(open("H:\Developer\Java work space\PythonStudy\chapter11\somefile.txt").readlines())

#write
f4=open("H:\Developer\Java work space\PythonStudy\chapter11\somefile2.txt","w")
f4.write("this\nis no\nhaiku\n")
f4.close()

#writelines
f5=open("H:\Developer\Java work space\PythonStudy\chapter11\somefile2.txt")
lines=f5.readlines()
f5.close()
lines[1]="isn't a\n"
f6=open("H:\Developer\Java work space\PythonStudy\chapter11\somefile2.txt","a")
f6.writelines(lines)
f6.close()
