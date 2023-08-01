# n=int(input())
# k=1



# while k<=n:
#     j=1
#     p=0
#     arr=[]
    
#     m=int(input())
#     while j<=m:
#         ps=[p]
#         lin=input()
#         arr.append(lin)
#         j+=1
    
#     for i in arr:
#         if (i.startswith("left")):
#             p=p-1
            
#         elif(i.startswith("right")):
#             p=p+1
            
#         else:
#             index = int(arr[i].split()[-1]) - 1
#             if index < i:
#                p += (p - ps[index])
#             else:
#                 p -= (ps[index] -p)
                
#         arr.append(p)
        
#     print(p)

#     k+=1
   

T = int(input())

for t in range(T):
    n = int(input())
    instructions = []
    position = 0
    positions = [position]
    
    for i in range(n):
        instructions.append(input().strip())
        
    for i in range(n):
        if instructions[i] == "LEFT":
            position -= 1
        elif instructions[i] == "RIGHT":
            position += 1
        else:
            index = int(instructions[i].split()[-1]) - 1
            while not index < i:
                index = int(instructions[index].split()[-1]) - 1
                
            position = positions[index]
                
        positions.append(position)
        
    print(position)