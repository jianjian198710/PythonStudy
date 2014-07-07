#6.4.4
def print_params(*params):
    print params

print_params(1,2,3)

#use * to collect left parameters return tuple
print "-----------use * to collect left parameters--------"
def print_params_2(title,*params):
    print title
    print params
    
print_params_2("Params:",1,2,3)

#use ** to collect keyword parameters, return dictionary
print "-----------use ** to collect keyword parameters--------"
def print_params_3(**params):
    print params

print_params_3(x=1,y=2,z=3)

def print_params_4(x,y,z=3,*pospar,**keypar):
    print x,y,z
    print pospar
    print keypar

print_params_4(1,2,3,4,5,6,7,foo=1,bar=2)

