#4.2
#crate dictionary manually
phonebook={"Alice":"2341","Beth":"9102","Cecil":"3258"}
print "Cecil's phone number is %(Cecil)s." %phonebook

#dict
items=[("name","Gumby"),("age",42)]
#create dictionary by dict
d=dict(items)
print "create d by dict: "+str(d)
d2=dict(name="Gumby",age=24)
print "create d2 by dict: "+str(d2)

#expamle4-1
people={
    "Alice":{
        "phone":"2341",
        "addr":"Foo drive 23"
    },
    "Beth":{
        "phone":"9102",
        "addr":"Bar Street 42"
    },
    "Cecil":{
        "phone":"3158",
        "addr":"Baz avenue 90"}
    }

name=raw_input("Name: ")
request=raw_input("phone number(p) or address(a)?")
if request=="p" : key="phone"
if request=="a" : key="addr"
labels={"phone":"phone number","addr":"address"}

if name in people: print "%s's %s is %s." %\
    (name,labels[key],people[name][key])
