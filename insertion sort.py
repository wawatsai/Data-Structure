import time
import random
Nothing_list = [random.randrange(10000) for _ in range(10000)]
start = time.time()
for i in range(1, len(Nothing_list)):
    number = Nothing_list[i]
    for j in range(i-1,-1,-1):
        if Nothing_list[j] > number:
            Nothing_list[j+1] = Nothing_list[j]
        else:
            j += 1
            break
    Nothing_list[j] = number
print(time.time()-start)
print(Nothing_list)