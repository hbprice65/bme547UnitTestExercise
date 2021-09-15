def solveForY(pair1, pair2, newX):
    m = (pair2[1]-pair1[1])/(pair2[0]-pair1[0])
    b = pair1[1]-pair1[0]*m
    y = newX*m+b
    return y
