n=int(input())
arr=list(map(int, input().split()))
k=int(input())
s_e=set()
p_f=False
for num in arr:
    if (k-num) in s_e:
        p_f=True
        break
    s_e.add(num)
if p_f:
    print("true")
else:
    print("false")
