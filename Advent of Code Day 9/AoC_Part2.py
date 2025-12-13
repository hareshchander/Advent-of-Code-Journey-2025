def solve():
    points = []
    
    try:
        with open('sample_input_9.txt', 'r') as f:
            data = f.read().strip()
    except FileNotFoundError:
        print("Error: input.txt not found.")
        return

    lines = [line for line in data.split('\n') if line.strip()]
    
    if not lines:
        print(0)
        return

    for line in lines:
        parts = line.split(',')
        x = int(parts[0])
        y = int(parts[1])
        points.append((x, y))
        
    unique_x = sorted(list(set(p[0] for p in points)))
    unique_y = sorted(list(set(p[1] for p in points)))
    
    map_x = {val: i * 2 + 1 for i, val in enumerate(unique_x)}
    map_y = {val: i * 2 + 1 for i, val in enumerate(unique_y)}
    
    width = len(unique_x) * 2 + 1
    height = len(unique_y) * 2 + 1
    
    grid = [[0] * width for _ in range(height)]
    
    count = len(points)
    
    for i in range(count):
        p1 = points[i]
        p2 = points[(i + 1) % count]
        
        cx1, cy1 = map_x[p1[0]], map_y[p1[1]]
        cx2, cy2 = map_x[p2[0]], map_y[p2[1]]
        
        if cy1 == cy2:
            start, end = min(cx1, cx2), max(cx1, cx2)
            for x in range(start, end + 1):
                grid[cy1][x] = 1
        else:
            start, end = min(cy1, cy2), max(cy1, cy2)
            for y in range(start, end + 1):
                grid[y][cx1] = 1
                
    stack = [(0, 0)]
    grid[0][0] = 2
    
    while stack:
        cx, cy = stack.pop()
        
        if cx + 1 < width and grid[cy][cx + 1] == 0:
            grid[cy][cx + 1] = 2
            stack.append((cx + 1, cy))
        if cx - 1 >= 0 and grid[cy][cx - 1] == 0:
            grid[cy][cx - 1] = 2
            stack.append((cx - 1, cy))
        if cy + 1 < height and grid[cy + 1][cx] == 0:
            grid[cy + 1][cx] = 2
            stack.append((cx, cy + 1))
        if cy - 1 >= 0 and grid[cy - 1][cx] == 0:
            grid[cy - 1][cx] = 2
            stack.append((cx, cy - 1))
            
    P = [[0] * (width + 1) for _ in range(height + 1)]
    
    for y in range(height):
        for x in range(width):
            is_valid = 0 if grid[y][x] == 2 else 1
            P[y+1][x+1] = is_valid + P[y][x+1] + P[y+1][x] - P[y][x]
            
    max_area = 0
    
    for i in range(count):
        for j in range(i + 1, count):
            p1 = points[i]
            p2 = points[j]
            
            orig_w = abs(p1[0] - p2[0]) + 1
            orig_h = abs(p1[1] - p2[1]) + 1
            real_area = orig_w * orig_h
            
            if real_area <= max_area:
                continue
            
            cx1, cy1 = map_x[p1[0]], map_y[p1[1]]
            cx2, cy2 = map_x[p2[0]], map_y[p2[1]]
            
            min_cx, max_cx = min(cx1, cx2), max(cx1, cx2)
            min_cy, max_cy = min(cy1, cy2), max(cy1, cy2)
            
            comp_w = max_cx - min_cx + 1
            comp_h = max_cy - min_cy + 1
            expected = comp_w * comp_h
            
            actual = (P[max_cy + 1][max_cx + 1] 
                    - P[min_cy][max_cx + 1] 
                    - P[max_cy + 1][min_cx] 
                    + P[min_cy][min_cx])
            
            if actual == expected:
                max_area = real_area
                
    print(max_area)

if __name__ == "__main__":
    solve()
