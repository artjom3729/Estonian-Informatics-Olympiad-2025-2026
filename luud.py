# loeme sisendi
m, n = (int(i) for i in input().split())

v = 0

if m > n:
    m, n = n, m

if m == 1:
    v = (n + 2) // 3
elif m == 2:
    v = 2 * ((n + 2) // 3)
else:
    v = (m * n + 2) // 3

# väljastame vastuse
print(int(v))
