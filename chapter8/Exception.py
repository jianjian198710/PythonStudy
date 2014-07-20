#8.3
#Use try/except to catch exception
try:
    x=input("Enter the first number: ")
    y=input("Enter the second number: ")
    print x/y
except ZeroDivisionError:
    print "The second number can't be zero!"
except TypeError:
    print "That isn't a number!"
    

#8.5
#Multiple exception with one try
try:
    x=input("Enter the first number: ")
    y=input("Enter the second number: ")
    print x/y
except (ZeroDivisionError,TypeError):
    print "The Input is wrong!"
    
#8.6
#Catch the excetpion
try:
    x=input("Enter the first number: ")
    y=input("Enter the second number: ")
    print x/y
except (ZeroDivisionError,TypeError), e:
    print e
    
#8.8
#keep input until there is no error
while True:
    try:
        x=input("Enter the first number: ")
        y=input("Enter the second number: ")
        value=x/y
        print "x/y is", value
    except Exception,e:
        print "Invalid input: ".e
        print "Please try again"
    else:
        break
        
        
