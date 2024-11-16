i = input().strip().split()
v_t = i[0]
c_t = i[1]
if v_t == c_t:
    r="NULL"
elif(v_t == 'R' and c_t == 'S') or \
    (v_t == 'P' and c_t == 'R') or \
    (v_t == 'S' and c_t == 'P'):
    r="Vignesh"
else:
    r="Charan"
print(r)
