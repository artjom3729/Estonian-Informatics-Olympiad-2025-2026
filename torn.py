n, w, l = (int(x) for x in input().split())
if w > l:
    w, l = l, w

b = []
for _ in range(n):
    b.append(sorted([int(x) for x in input().split()]))

dp = [[0] * 3 for _ in range(n)]
v = 0

for i in range(n):
    d = b[i]
    opts = [(d[0], d[1], d[2]), (d[1], d[0], d[2]), (d[2], d[0], d[1])]

    for k in range(3):
        h, cw, cl = opts[k]
        cur = 0

        if cw <= w and cl <= l:
            cur = h

        for j in range(i):
            pd = b[j]
            popts = [(pd[1], pd[2]), (pd[0], pd[2]), (pd[0], pd[1])]
            for m in range(3):
                if dp[j][m] == 0:
                    continue
                pw, pl = popts[m]
                if cw <= pw and cl <= pl:
                    if dp[j][m] + h > cur:
                        cur = dp[j][m] + h

        dp[i][k] = cur
        if cur > v:
            v = cur
print(v)
