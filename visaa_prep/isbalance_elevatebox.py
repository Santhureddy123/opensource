N=int(input())
A=list(map(int,input().split()))
b=[]
for i in range(N):
    l_w=sum(A[:i])
    r_w=sum(A[i+1:])
    bal=abs(l_w-r_w)
    b.append(bal)
print(" ".join(map(str, b)))
