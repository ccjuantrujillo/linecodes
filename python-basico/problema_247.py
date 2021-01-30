M = [[1,0,0],[0,1,0],[0,0,1]]

s = 0.0

for i in range(0,3):
    for j in range(0,3):
        s += M[i][j]

print s/9.0