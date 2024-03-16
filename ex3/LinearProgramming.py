# linear programming
# Max 3x + 2y + 5z
# s.t. x+y <= 10
#      2x+z <= 9
#      y+2z <= 11
#      x, y, z >= 0
# Min z = 35x + 25y
# s.t. 0.32x + 0.22y >= 8
#      0.11x + 0.09y >= 3
#      0.15x + 0.15y >= 4
#      x, y >= 0

def f(p):
    x = p[0]
    y = p[1]
    z = p[2]
    return 3*x + 2*y + 5*z

    
print(f([1, 2, 3]))