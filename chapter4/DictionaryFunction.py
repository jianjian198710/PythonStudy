#4.2.4
from copy import deepcopy
#clear
d={}
d["name"]="Gumby"
d["age"]=42
print "d is: "+str(d)
print "d.clear() is: "+str(d.clear())

#copy shallow copy: origin and copy point one object
x={"username":"admin","machines":["foo","bar","baz"]}
y=x.copy()
#replace a value, the origin x is not changed(replace will return a new string)
y["username"]="mlh"
#modify a value, the origin x is changed(remove return the origin string)
y["machines"].remove("baz")
print "y is: "+str(y)
print "x is: "+str(x)

#deepcopy: origin and copy point different objects
a={}
a["names"]=["Alfred","Bertrand"]
b=a.copy()
c=deepcopy(a)
a["names"].append("Clive")
print "b is: "+str(b)
print "c is: "+str(c)

#fromkeys: create the new dictionary with the given key
e={}.fromkeys(["name","age"])
print "fromkeys is: "+str(e)

e={}.fromkeys(["name","age"],"unknown")
print "fromkey is: "+str(e)

#get: return none when the key doesn't exist
d={}
print "use get: "+str(d.get("name"));

#has_key:
d={}
print "has_key is: "+str(d.has_key("name"))
d["name"]="Eric"
print "has_key is: "+str(d.has_key("name"))

#items: return the dictionary as a list
d={"title":"Python Web Site","url":"http://www.python.org","spam":"0"}
print "items: "+str(d.items())

#iteritems: return the iterator
it=d.iteritems()
print "it is: "+str(it)
print "list(it) is: "+str(list(it))

#keys && iterkeys
print "keys is: "+str(d.keys())

#pop: return the value with the given key and then remove the key-value
d={"x":"1","y":"2"}
print "pop is: "+d.pop("x")
print "d is: "+str(d)

#popitem: remove a key-value with random
d={"title":"Python Web Site","url":"http://www.python.org","spam":"0"}
print "popitem is: "+str(d.popitem())
print "d is: "+str(d)

#setdefault: set the key with the default value when the key doesn't exist
print "Test setdefault!!!"
d={}
d.setdefault("name","N/A")
print "d is: "+str(d)
d["name"]="Gumby"
d.setdefault("name","N/A")
print "d is: "+str(d)

#update: update one dictionary with another
print "Test update!!!"
d={"title":"Python Web Site","url":"http://www.python.org","spam":"0"}
x={"title":"Python Language Website"}
d.update(x)
print "d is: "+str(d)

#values && itervalue
print "Test values!!!"
d={"title":"Python Web Site","url":"http://www.python.org","spam":"0"}
print "values is: "+str(d.values())