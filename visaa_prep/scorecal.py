T = int(input().strip())
for _ in range(T):
    X, N = map(int, input().strip().split())
    p_t_c=X//10
    s=p_t_c*N
    print(s)
