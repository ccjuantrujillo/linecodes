def incremento(a):
    return lambda x:x+a

f = incremento(43)
f(0)
f(1)
print(f(10))
