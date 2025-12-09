def solve():
    with open('sample_input_8.txt', 'r') as f:
        lines = f.read().strip().split('\n')

    points = []
    for line in lines:
        parts = line.split(',')
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        points.append((x, y, z))

    n = len(points)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            
            dist = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
            edges.append((dist, i, j))

    edges.sort()

    parents = list(range(n))

    def find_root(node):
        while node != parents[node]:
            node = parents[node]
        return node

    limit = 1000
    if len(edges) < 1000:
        limit = len(edges)

    for k in range(limit):
        dist, i, j = edges[k]
        root_i = find_root(i)
        root_j = find_root(j)

        if root_i != root_j:
            parents[root_j] = root_i

    sizes = {}
    for i in range(n):
        root = find_root(i)
        if root in sizes:
            sizes[root] += 1
        else:
            sizes[root] = 1

    size_list = list(sizes.values())
    size_list.sort(reverse=True)

    result = 1
    count = 0
    for s in size_list:
        result = result * s
        count += 1
        if count == 3:
            break

    print(result)

solve()
