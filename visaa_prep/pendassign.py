i_v = input().strip().split()
x = int(i_v[0])
y = int(i_v[1])
z = int(i_v[2])
t_t=z*24*60
t_n=x*y
if t_n <=t_t:
    r="YES"
else:
    r="NO"
print(r)
