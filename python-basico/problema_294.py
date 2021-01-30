def productoria(a,b):
    s = 1
    if a > b or a < 0 or b < 0:
        return 0
    else:
        for i in range(a,b+1):
            s = s * i

    return s

print productoria(-4,-2)