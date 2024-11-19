n=int(input())
arr=list(map(int, input().split()))
k=int(input())
k=k%n
r_arr=arr[-k:]+arr[:-k]
print(" ".join(map(str, r_arr)))
