import sys

# loeme aukude ja punnide arvud
n, m = (int(x) for x in input().split())

# leiame vastuse
v = [-1] * m

def solve(punn_alg, punn_lopp, auk_alg, auk_lopp):
    if punn_alg > punn_lopp:
        return

    punn_kesk = (punn_alg + punn_lopp) // 2

    vastus = n + 1

    madal = auk_alg
    suur = min(auk_lopp, n)

    if madal <= suur:
        l, r = madal, suur
        leitud = -1

        while l <= r:
            kesk_h = (l + r) // 2

            print("?", punn_kesk + 1, kesk_h, flush=True)
            res = int(sys.stdin.readline())

            if res == 1:
                leitud = kesk_h
                r = kesk_h - 1
            else:
                l = kesk_h + 1

        if leitud != -1:
            vastus = leitud
        else:
            vastus = n + 1
    else:
        vastus = n + 1

    if vastus <= n:
        v[punn_kesk] = vastus
    else:
        v[punn_kesk] = -1
        vastus = n + 1

    solve(punn_alg, punn_kesk - 1, auk_alg, vastus)

    solve(punn_kesk + 1, punn_lopp, vastus, auk_lopp)

solve(0, m - 1, 1, n + 1)

# väljastame vastuse
print("!", *v, flush=True)
