graph = {
    0: [1, 2],
    1: [2],
    2: [],
    3: [1],
    4: []
}

count = 0

for node in graph:
    if len(graph[node]) == 0:
        count += 1

print("Number of sink nodes:", count)