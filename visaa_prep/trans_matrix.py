n=int(input())
m=[]
for _ in range(n):
    row=list(map(int,input().split()))
    m.append(row)
t=[[m[j][i] for j in range(n)] for i in range(n)]
for row in t:
    print(" ".join(map(str, row)))
