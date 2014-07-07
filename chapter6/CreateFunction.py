#6.3
def hello(name):
    return "Hello, "+name+"!";

print hello("Peter")

def fib(num):
    result=[0,1]
    for _i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

print fib(10)