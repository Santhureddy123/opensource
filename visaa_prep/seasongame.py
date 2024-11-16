M = int(input())
if M < 1 or M > 12:
    r = "Invalid"
else:
    if M in [3, 4, 5]:
        r = "Spring"
    elif M in [6, 7, 8]:
        r = "Summer"
    elif M in [9, 10, 11]:
        r = "Autumn"
    elif M in [12, 1, 2]:
        r = "Winter"
print(r)
