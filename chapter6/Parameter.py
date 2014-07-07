#6.4
def init(data):
    data["first"]={}
    data["middle"]={}
    data["last"]={}

storage={}
init(storage)
print "storage is: "+str(storage)

def lookup(data,label,name):
    return data[label].get(name)

def store(data,full_name):
    names=full_name.split()
    if len(names)==2: names.insert(1,"")
    labels='first','middle','last'
    for label,name in zip(labels,names):
        people=lookup(data,label,name)
        #people not empty
        if people:
            people.append(full_name)
        else:
            data[label][name]=[full_name]

#test
MyNames={}
init(MyNames)
store(MyNames,"Magnus Lie Hetland")
print "lookup result is1: "+str(lookup(MyNames,"middle","Lie"))

store(MyNames,"Robin Hood")
store(MyNames,"Robin locksley")
print "lookup result is2: "+str(lookup(MyNames,"first","Robin"))
print "lookup result is3: "+str(lookup(MyNames,"middle",""))