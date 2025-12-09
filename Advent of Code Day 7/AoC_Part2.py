def solve():
    with open('sample_input_7.txt', 'r') as f:
        grid = f.read().splitlines()
        
    if not grid:
        return

    rows = len(grid)
    cols = len(grid[0])
    
    # Instead of a set, we use a list of numbers to count timelines per column
    current_counts = [0] * cols
    
    # Find start position
    for c in range(cols):
        if grid[0][c] == 'S':
            current_counts[c] = 1
            break
            
    # Process row by row
    for r in range(rows):
        next_counts = [0] * cols
        active_particles = False
        
        for c in range(cols):
            # If there are timelines at this column
            if current_counts[c] > 0:
                char = grid[r][c]
                
                if char == '^':
                    # Split: Add current count to both Left and Right neighbors
                    if c - 1 >= 0:
                        next_counts[c - 1] = next_counts[c - 1] + current_counts[c]
                    if c + 1 < cols:
                        next_counts[c + 1] = next_counts[c + 1] + current_counts[c]
                else:
                    # Pass through: Add current count to the same column in next row
                    next_counts[c] = next_counts[c] + current_counts[c]
                    
                active_particles = True
                
        if active_particles == False:
            break
            
        current_counts = next_counts
        
    # The answer is the sum of all timelines at the bottom
    total = sum(current_counts)
    print(total)

solve()
