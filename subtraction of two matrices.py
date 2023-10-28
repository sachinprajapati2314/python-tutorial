x = [[11,5,9],
     [4,8,17],
     [8,12,3]]

y = [[5,6,2],
     [7,2,4],
     [9,4,6]]

z = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        z[i][j] = x[i][j] - y[i][j]

for r in z:
    print(r)