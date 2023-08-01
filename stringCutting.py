while True:
    N = int(input())
    if N == 0:
        break
        
    k = int(input())
    cuts = list(map(int, input().split()))
    s = input().strip()
    
    cuts.sort()
    cuts = [0] + cuts + [len(s)]
    
    cost = 0
    for i in range(1, len(cuts)):
        s1 = s[cuts[i-1]:cuts[i]]
        s2 = s[cuts[i]:cuts[i+1]]
        cost += abs(len(s1) - len(s2))
        
    print(cost)