def a_marks(N, X, Y):
    for i in range(N + 1):
            if i * X == Y:
                return "YES" 
    return "NO"
input_values = input().strip().split()
N = int(input_values[0])
X = int(input_values[1])
Y = int(input_values[2])
result = a_marks(N, X, Y)
print(result)
                    
