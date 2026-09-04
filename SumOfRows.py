
x = [[8, 2, 3],
     [4, 1, 9],
     [1, 4, 8]]

for i in range(len(x)):
    total = 0

    for j in range(len(x[0])):
        total = total + x[i][j]

    print(total)