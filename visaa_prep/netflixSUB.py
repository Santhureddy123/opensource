i_v=input().strip().split()
A = int(i_v[0])
B = int(i_v[1])
C = int(i_v[2])
X = int(i_v[3])

if A+B>=X or A+C>=X or B+C>=X: 
    result= "YES"
else:
    result= "NO"
print(result)
