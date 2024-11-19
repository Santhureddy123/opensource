n=int(input())
s=list(map(int, input().split()))
s.sort(reverse=True)
for i in range(n-2):
    a,b,c= s[i],s[i+1],s[i+2]
    if a<b+c:
        print(a+b+c)
        break
else:
    print(-1)
