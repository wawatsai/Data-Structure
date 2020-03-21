import time
t = time.time()
memory = {0: 0, 1: 1, 2: 1}
def Function_fibonacci(fibonacci):
    if fibonacci in memory: return memory[fibonacci]
    elif fibonacci < 0: return 0
    correct = Function_fibonacci(fibonacci-1) + Function_fibonacci(fibonacci-2)
    memory[fibonacci] = correct
    return correct
print(Function_fibonacci(2000))
print(time.time() - t)
#
#
#
#
#
#
#
#
#
#input_f = int(input("Please input a number that is not over 37: "))
#from functools import lru_cache as cache    #fast catch
#t = time.time()
#@cache()
#def fibonacci(fi):
#    print("In function!")
#    if fi < 3 and fi > 0: return 1
#    elif fi < 1: return 0
#    return fibonacci(fi-1) + fibonacci(fi-2)
#print(fibonacci(input_f))
#print(time.time() - t) 
#
#
#
#
#
#
#
#
#
#
while True:
    input_fibonacci = int(input("Please input a number that is not over 1500: "))
    t = time.time()
    def Fibonacci_iterative(f):
        if f < 3 and f > 0: return 1
        elif f < 1: return 0
        a = b = 1
        for i in range(2, f):
            a, b = b, a+b
        return b
    print(Fibonacci_iterative(input_fibonacci))
    print(time.time() - t)
#    
#
#
#
#
#
#
#
#
#
#
#
#