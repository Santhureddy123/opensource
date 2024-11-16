n=int(input())
neg=n<0
n=abs(n)
r_n=int(str(n)[::-1])
if neg:
    r_n = -r_n
if r_n < -2**31 or r_n > 2**31 -1:
    r_n = 0
print(r_n)
