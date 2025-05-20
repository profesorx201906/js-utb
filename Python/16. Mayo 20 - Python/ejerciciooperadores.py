a = 10
b = 12
c = 13
d = 10

print(((a > b) or (a < c)) and ((a == c) or (a >= b)))  # T - F - T

print(((a >= b) or (a < d)) and ((a >= d) and (c > d)))  # T - F - T

print(not (a == c) and (c > b))  # T - T - F
