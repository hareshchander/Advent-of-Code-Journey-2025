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
    groups_count = n

    def find_root(node):
        while node != parents[node]:
            node = parents[node]
        return node

    for edge in edges:
        dist, i, j = edge
        
        root_i = find_root(i)
        root_j = find_root(j)

        if root_i != root_j:
            parents[root_j] = root_i
            groups_count = groups_count - 1
            
            if groups_count == 1:
                point_1_x = points[i][0]
                point_2_x = points[j][0]
                print(point_1_x * point_2_x)
                break

solve()
