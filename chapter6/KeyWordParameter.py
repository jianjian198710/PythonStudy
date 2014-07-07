#6.4.3
def hello_1(greeting,name):
    print "%s, %s!" %(greeting,name)
    
hello_1(greeting="Hello",name="World")
hello_1(name="World",greeting="Hello")

#default value
def hello_3(greeting="Hello",name="World"):
    print "%s, %s!" %(greeting,name)

hello_3()
hello_3("Greeting","Universe")
hello_3(name="Universe")