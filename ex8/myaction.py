def myaction(status):
    Rlimit = 0.1
    Llimit = -0.1
    angLimitR = .1
    angLimitL = -.1
    carPos, carV, poleAng, poleAngV = status
    if poleAng > 0:
        if poleAngV > 0:
            action= 1
        elif poleAngV < 0:
            if carPos > 0:
                if carPos < Rlimit: 
                    action = 0
                elif carPos > Rlimit: action = 1
            elif carPos < 0: action = 0
    elif poleAng < 0:
        if poleAngV < 0: action = 0
        elif poleAngV > 0:
            if carPos < 0:
                if carPos > Llimit:
                    action = 1
                elif carPos < Llimit: action = 0 
            elif carPos > 0: action = 1
    return action