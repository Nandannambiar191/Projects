# First matrix
x = [[8, 2, 3],
     [4, 1, 9],
     [1, 4, 8]]

# Second matrix
y = [[2, 1, 1],
     [1, 1, 2],
     [1, 2, 3]]

# Matrix to store the answer
answer = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Subtract the matrices
for i in range(len(x)):
    for j in range(len(x[0])):
        answer[i][j] = x[i][j] - y[i][j]

# Print the answer
for r in answer:
    print(r)