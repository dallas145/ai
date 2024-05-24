import numpy as np
from numpy.linalg import norm
from engine import Value


def gradientDescendent(f, p0, h=0.01, max_loops=100000, dump_period=1000):
    p = p0.copy()
    for i in range(max_loops):
        fp = f(p)
        fp.backward()
        gp = []
        for param in p:
            gp.append(param.grad)
        glen = norm(gp) # norm = 梯度的長度 (步伐大小)
        if glen < 0.00001: # 如果步伐已經很小了，那麼就停止吧！
            break
        gh = np.multiply(gp, -1*h) # gh = 逆梯度方向的一小步
        p +=  gh # 向 gh 方向走一小步
    print(p)
    return p # 傳回最低點！

    
def f(p):
    [x, y, z] = p
    return (x-1)**2 + (y-2)**2 + (z-3)**2
    

p = [Value(0), Value(0), Value(0)]
print("Value of the lowest point = ", f(gradientDescendent(f,p)))