def solve():
    points = []
    
    with open('sample_input_9.txt', 'r') as f:
        data = f.read().strip()
        
    lines = data.split('\n')
    
    for line in lines:
        parts = line.split(',')
        x = int(parts[0])
        y = int(parts[1])
        points.append((x, y))
        
    max_area = 0
    count = len(points)
    
    for i in range(count):
        for j in range(i + 1, count):
            p1 = points[i]
            p2 = points[j]
            
            x1 = p1[0]
            y1 = p1[1]
            x2 = p2[0]
            y2 = p2[1]
            
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            
            area = width * height
            
            if area > max_area:
                max_area = area
                
    print(max_area)

solve()
