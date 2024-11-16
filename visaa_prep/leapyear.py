Y = int(input().strip())
if (Y % 4 == 0 and Y % 100 != 0) or (Y%400==0):
    result = "YES"
else:
    result="NO"
print(result)
