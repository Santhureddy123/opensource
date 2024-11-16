i_v = input().strip().split()
X = int(i_v[0])
N = int(i_v[1])
c_p = 100
t_c = X * c_p
p_r = max(N - t_c, 0)
a_r = (p_r + c_p - 1) // c_p
print(a_r)
