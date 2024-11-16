n=int(input())
a_r=list(map(int,input().split()))
max_absences=0
c_s=0
for day in a_r:
    if day==0:
        c_s += 1
        if c_s>max_absences:
            max_absences=c_s
    else:
        c_s=0
print(max_absences)
