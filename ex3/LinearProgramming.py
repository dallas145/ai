import random
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
    x, y, z = p[0], p[1], p[2]
    if x + y <= 10 and 2*x + z <= 9 and y + 2*z <= 11 and x >= 0 and y >= 0 and z >= 0:
        return 3*x + 2*y + 5*z
    else:
        return -1


p = [0, 0, 0]
pv = 0
fail = 0

while fail < 100000:
    nP = p.copy()
    for i in range(len(nP)):
        nP[i] += random.uniform(-1, 1)
    nPv = f(nP)
    
    if nPv > pv:
        p = nP
        pv = nPv
        print(pv)
    else:
        fail += 1
        
    
print()
print(f'max= {pv:.4f}')
print(f'x= {p[0]:.4f}, y= {p[1]:.4f}, z= {p[2]:.4f}')