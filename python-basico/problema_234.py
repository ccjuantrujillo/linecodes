a = [1,-2,1,-5,0,3,2,4,6,1,3,5,4]

var = len(a)

i = 0

while i < var:
    if a[i] % 2 == 0:        
        del a[i]
    else:
        i = i + 1
    var = len(a)
print a