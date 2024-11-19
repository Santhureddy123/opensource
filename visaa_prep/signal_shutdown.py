n,m=map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r_set=set()
c_set=set()
for i in range(n):
    for j in range(m):
        if grid[i][j]==0:
            r_set.add(i)
            c_set.add(j)
for i in range(n):
    for j in range(m):
        if i in r_set or j in c_set:
            grid[i][j]=0
for row in grid:
    print(" ".join(map(str, row)))
            
