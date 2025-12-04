m, n = (int(i) for i in input().split())
s = list(map(int, str(input())))

r = []
if len(s) > 0:
    c = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            c += 1
        else:
            r.append(c)
            c = 1
    r.append(c)

if len(r) > m:
    print(0)
else:
    d = [0] * (m + 1)
    d[0] = 1
    mod = 2147483648

    for x in r:
        nd = [0] * (m + 1)
        cs = 0
        for i in range(1, m + 1):
            cs += d[i - 1]
            if i - x - 1 >= 0:
                cs -= d[i - x - 1]
            nd[i] = cs % mod
        d = nd

    print(d[m])
