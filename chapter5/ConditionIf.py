#5.4.2 if
name=raw_input("what is your name? ")
if name.endswith("Gumby"):
    if name.startswith("Mr."):
        print "Hello, Mr."+name
    elif name.startswith("Mrs."):
        print "Hello, Mrs."
    else:
        print "Hello, "+name
else:
    print "Hello, Stranger"
    
num=input("Enter a number: ")
if num<0:
    print "The number is negative"
elif num>0:
    print "The number is positive"
else:
    print "The number is zero"

number=input("Enter a number between 1 and 10: ")
if 1<=number<=10:
    print "Great!"
else:
    print "Wrong!"
    
#assert
age=10
assert 0<age<100
# age=-100
assert 0<age<100, "The age is wrong!"

#for
words=["this","","","",]
