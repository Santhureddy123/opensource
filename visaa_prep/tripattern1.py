N=int(input())
c_n=1
for i in range(1,N + 1):
    for j in range(i):
        print(c_n, end=' ')
        c_n+=1
    print()
