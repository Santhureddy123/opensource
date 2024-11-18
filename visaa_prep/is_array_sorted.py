n=int(input())
arr=list(map(int, input().split()))
is_sort = True
for i in range(1, n):
    if arr[i]<arr[i-1]:
        is_sort=False
        break
print("true" if is_sort else "false")
        
