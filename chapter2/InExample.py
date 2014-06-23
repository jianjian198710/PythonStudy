#Example2-4

database=[["Tom",1234],["Mary",2345],["Peter",3456],["Mike",4567]]

name=raw_input("User Name: ")
pin=int(raw_input("PIN code: "))

if [name,pin] in database:
    print "Access Granted!"