import time
import random
data = [random.randrange(10000) for _ in range(10000)]
start = time.time()
print(sorted(data))
print(time.time()-start)