# loeme sisendi
n, m = (int(x) for x in input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

# leiame vastuse
c = []
j = 0

for i in b:
    while j < n and a[j] < i:
        j += 1
    
    if j < n:
        c.append(str(j + 1))
    else:
        c.append("-1")

# väljastame vastuse
for x in c:
    print(x)