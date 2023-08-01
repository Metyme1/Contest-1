def smallest_period(s):
    n = len(s)
    for k in range(1, n+1):
        if n % k == 0:
            repeats = n // k
            pattern = s[:k]
            if pattern * repeats == s:
                return k
    return n


t = int(input())
input()
c = t
for i in range(t):
    s = input()
    period = smallest_period(s)
    c -= 1
    if(c >= 1):
        print(period)
        print()
    else:
        print(period)