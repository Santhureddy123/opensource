s=input()
r=""
for i in s:
    a=ord(i)
    if 97<=a<=122:
        r+=chr(a-32)
    else:
        r+=chr(a+32)
print(r)
