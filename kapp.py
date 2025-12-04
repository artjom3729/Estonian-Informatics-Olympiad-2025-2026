m, n = (int(i) for i in input().split())
s = list(map(int, str(input())))

koodid = []
pikkus = 1
kood = [s[0]]

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        kood.append(s[i])
    else:
        kood.append(s[i-1])
        kood.append(s[i])

print(kood)
if len(kood) > m:
    print(0)
