#6.5
#use globals() to avoid the local parameter override the global parameter when they have the same name
def combine(parameter):
    print parameter+globals()["parameter"]

parameter="berry"
combine("Shrub")

#Closure
def multiplier(factor):
    def multiplyByFactor(number):
        return number*factor
    return multiplyByFactor

double=multiplier(2)
print "clousre result is: "+str(double(5))




