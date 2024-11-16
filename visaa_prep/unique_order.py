N=int(input())
arr=list(map(int,input().split()))
u_e=[]
s_e=set()
for ele in arr:
    if ele not in s_e:
        u_e.append(ele)
        s_e.add(ele)
print(" ".join(map(str, u_e)))
