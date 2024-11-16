n=int(input())
arr=list(map(int,input().split()))
r_a=arr[1:]+[arr[0]]
print(" ".join(map(str,r_a)))
