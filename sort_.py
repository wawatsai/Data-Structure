a = [123, 22, 777, 111,234,455,666,333,876,544,779,700]
b = max(a)
c = min(a)
for _ in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)
print(b)
print(c)
print(sorted(a))
print("ok")
a = [5,4,3,2,1]
for _ in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)
print(sorted(a))