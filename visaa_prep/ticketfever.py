T=int(input())
for _ in range(T):
    N, M = map(int, input().split())
    s_t=max(0, N - M)
    print(s_t)
