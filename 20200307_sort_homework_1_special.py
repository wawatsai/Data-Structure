import time
import random
time_start = time.time()
a = [234, 566, 34, 9, 333, 122, 678, 55, 7777, 8888, 1234, 6754]
b = []
while a:
    b.append(min(a))
    a.remove(min(a))
print(b)
print(sorted(b))
end = time.time()
print("The time is:", end - time_start)