import time
a = [234, 566, 34, 9, 333, 122]
start = time.time()
for _ in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
print(a)
print(sorted(a))
end = time.time()
print(end - start)