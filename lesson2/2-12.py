#統計検定量Uを求める式

def toukeiryou(nA,nB,RA,RB):
    U1 = nA*nB + 0.5*nA*(nA+1)-RA
    U2 = nA*nB + 0.5*nB*(nB+1)-RB
    if U1 > U2:
        return U2
    else:
        return U1
    
    
print(toukeiryou(8,8,45,88))