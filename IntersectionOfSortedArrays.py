array1 = [1, 2, 3, 4]
array2 = [3, 4, 5, 6]
union = []

for x in array1:
    if x not in union:
        union.append(x)

for x in array2:
    if x not in union:
        union.append(x)


intersection = []
for x in array1:
    if x in array2:
        intersection.append(x)
print("Union:", union)
print("Intersection:", intersection)