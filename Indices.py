def evansA3(a0,a1,b,c0,c1):
    #Index for joint distribution q(a0,a1,b,c0,c1) for evans scenario where |A|=3, |B|=|C|=2.
    i=0
    for C1 in range(2):
        for C0 in range(2):
            for B in range(2):
                for A1 in range(3):
                    for A0 in range(3):
                        if C1==c1 and C0==c0 and B==b and A1==a1 and A0==a0 :
                            return i
                        else :
                            i=i+1

def evansmarginalA3(a0,a1,c0,c1):
    #Index for marginal joint distribution q(a0,a1,c0,c1) for evans scenario where |A|=3, |C|=2.
    i=0
    for C1 in range(2):
        for C0 in range(2):
            for A1 in range(3):
                for A0 in range(3):
                    if C1==c1 and C0==c0 and A1==a1 and A0==a0 :
                        return i
                    else :
                        i=i+1

def evansAmarginalA3(a0,a1):
    #Index for Alice's marginal  joint distribution q(a0,a1) for evans scenario where |A|=3.
    i=0
    for A1 in range(3):
        for A0 in range(3):
            if A1==a1 and A0==a0 :
                return i
            else :
                i=i+1

def evansCmarginalA3(c0,c1):
    #Index for marginal joint distribution q(c0,c1) for evans scenario where |C|=2.
    i=0
    for C1 in range(2):
        for C0 in range(2):
            if C1==c1 and C0==c0:
                return i
            else :
                i=i+1                
def evansObIndexA3(a,b,c):
    i=0
    for C in range(2):
        for B in range(2):
            for A in range(3):
                if A==a and B==b and C==c:
                    return i
                else:
                    i=i+1
def evansObIndexA4(a,b,c):
    i=0
    for C in range(2):
        for B in range(2):
            for A in range(4):
                if A==a and B==b and C==c:
                    return i
                else:
                    i=i+1
def evansA4(a0,a1,b,c0,c1):
    #Index for joint distribution q(a0,a1,b,c0,c1) for evans scenario where |A|=3, |B|=|C|=2.
    i=0
    for C1 in range(2):
        for C0 in range(2):
            for B in range(2):
                for A1 in range(4):
                    for A0 in range(4):
                        if C1==c1 and C0==c0 and B==b and A1==a1 and A0==a0 :
                            return i
                        else :
                            i=i+1

def evansmarginalA4(a0,a1,c0,c1):
    #Index for marginal joint distribution q(a0,a1,c0,c1) for evans scenario where |A|=3, |C|=2.
    i=0
    for C1 in range(2):
        for C0 in range(2):
            for A1 in range(4):
                for A0 in range(4):
                    if C1==c1 and C0==c0 and A1==a1 and A0==a0 :
                        return i
                    else :
                        i=i+1

def evansAmarginalA4(a0,a1):
    #Index for Alice's marginal  joint distribution q(a0,a1) for evans scenario where |A|=3.
    i=0
    for A1 in range(4):
        for A0 in range(4):
            if A1==a1 and A0==a0 :
                return i
            else :
                i=i+1

def evansCmarginalA4(c0,c1):
    #Index for marginal joint distribution q(c0,c1) for evans scenario where |C|=2.
    i=0
    for C1 in range(2):
        for C0 in range(2):
            if C1==c1 and C0==c0:
                return i
            else :
                i=i+1                      