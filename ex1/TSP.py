from random import *
# citys = [
#     (0,0), (0,1), (0,2),
#     (1,2), (2,2),
#     (2,1), (2,0), (1,0)
# ]
# citys = [
#     (0,0), (0,1), (2,0),
#     (1,0), (2,2),
#     (0,2), (1,2), (2,1)
# ]
citys = [
    (0,3),(0,0),
    (0,2),(0,1),
    (1,0),(1,3),
    (2,0),(2,3),
    (3,0),(3,3),
    (3,1),(3,2)
]

cLen = len(citys)
path = [(i+1) % cLen for i in range(cLen)]

def distance(p1, p2):
    # print("p1=", p1)
    x1, y1 = p1
    x2, y2 = p2
    dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return dist

def pathLength(p):
    dist = 0
    for i in range(len(p)):
        pNow = p[i]
        if (i+1) < len(p):
            pNext = p[i+1]
        else:
            pNext = p[0]
        dist += distance(citys[pNow], citys[pNext]) 
    return dist

def nextP(p):
    pL = len(p) - 1
    pN = p.copy()
    N1 = randint(0, pL)
    N2 = randint(0, pL)
    pN[N1], pN[N2] = pN[N2], pN[N1]
    return pN

def hillClimb(p, max_fail=10000):
    fail = 0
    while True:
        p1 = nextP(p)
        if pathLength(p1) < pathLength(p):
            p = p1
            fail = 0
        else:
            fail += 1
            if fail > max_fail:
                return [p, pathLength(p)]
            

final = hillClimb(path)
print("path= ", final[0], "\nLength= ", final[1])
# print(hillClimb(path))
