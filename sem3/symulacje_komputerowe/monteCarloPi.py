import random

def monteCarloPi(n):
    pointsInsideCircle = 0
    pointsTotal = 0

    for i in range(n):
        if random.random()**2 + random.random()**2 <= 1:
            pointsInsideCircle += 1
        pointsTotal += 1

    return 4 * pointsInsideCircle / pointsTotal