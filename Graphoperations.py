def minimum_swaps(arr):
    sorted_arr = sorted(arr)
    swaps = 0

    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            j = arr.index(sorted_arr[i])
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1

    return swaps


arr = list(map(int, input().split()))
print(minimum_swaps(arr))