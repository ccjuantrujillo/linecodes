def sumatoria(a,b):
    s = 0
    if a > b:
        return 0
    else:
        for i in range(a,b+1):
            s = s + i

    return s

print sumatoria(3,7)