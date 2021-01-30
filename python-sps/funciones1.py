from math import sqrt
a = 2
b = 4
c = 3

def area_triangulo(a,b,c):
    s = (a+b+c)/2.0
    return sqrt(s*(s-a)*(s-b)*(s-c))

print(area_triangulo(1,3,2.5))
#print a
