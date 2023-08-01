n=int(input())
for i in range(n):
    s = input()
    l = len(s)
    period = l
    for j in range(1, l+ 1):
        if l % j == 0:
            
            for k in range(j, l):
                if s[k] != s[k % j]:
                    re = False
                    break
            if re:
                period = j
                break
    print(period)
    if i < n - 1:
        print() 
        

        
        