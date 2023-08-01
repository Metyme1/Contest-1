# n=int(input())
# i=0
# while i<n:
#     count=0
#     m=input()
#     for j in m:
#         if j=="O":
#             count+=1
#             con=+count
#         else:
#             con=0
#     print(con)
#     i+=1

t = int(input()) 

for _ in range(t):
    s = input()
    score = 0 
    con= 0 
    for c in s:
        if c == 'O':
            con+= 1
            score += con
            
        else:
            con= 0
    print(score)