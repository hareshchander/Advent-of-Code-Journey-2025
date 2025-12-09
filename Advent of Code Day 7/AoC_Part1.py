def solve():
    split_count = 0
    
    with open('sample_input_7.txt', 'r') as f:
        grid = f.read().splitlines()
        
    if not grid:
        return

    rows = len(grid)
    cols = len(grid[0])
    
    current_beams = set()
    
    for c in range(cols):
        if grid[0][c] == 'S':
            current_beams.add(c)
            break
            
    for r in range(rows):
        next_beams = set()
        
        if len(current_beams) == 0:
            break
            
        for c in current_beams:
            if c < 0 or c >= cols:
                continue
                
            char = grid[r][c]
            
            if char == '^':
                split_count = split_count + 1
                next_beams.add(c - 1)
                next_beams.add(c + 1)
            elif char == '.':
                next_beams.add(c)
            elif char == 'S':
                next_beams.add(c)
                
        current_beams = next_beams
        
    print(split_count)

solve()
