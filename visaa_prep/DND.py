f_l=input().split()
n=int(f_l[0])
m=int(f_l[1])
arr=list(map(int, input().split()))
num1=0
num2=0
for num in arr:
    if num %m ==0:
        num2+= num
    else:
        num1+= num
res=num2-num1
print(res)
