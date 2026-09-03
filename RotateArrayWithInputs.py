arr = [10, 20, 30, 40, 50]
for i in range(3):
    first = arr.pop(0)
    arr.append(first)
print(arr)