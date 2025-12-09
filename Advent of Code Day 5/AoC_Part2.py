def solve():
    with open('sample_input_5.txt', 'r') as f:
        content = f.read().strip()
        
    parts = content.split('\n\n')
    range_lines = parts[0].split('\n')
    
    ranges = []
    for line in range_lines:
        nums = line.split('-')
        start = int(nums[0])
        end = int(nums[1])
        ranges.append((start, end))
        
    # Sort ranges so we can merge them easily
    ranges.sort()
    
    merged = []
    if len(ranges) > 0:
        current_start, current_end = ranges[0]
        
        for i in range(1, len(ranges)):
            next_start, next_end = ranges[i]
            
            # If ranges overlap or touch, merge them
            if next_start <= current_end + 1:
                current_end = max(current_end, next_end)
            else:
                merged.append((current_start, current_end))
                current_start = next_start
                current_end = next_end
                
        merged.append((current_start, current_end))
        
    total_count = 0
    for start, end in merged:
        total_count += (end - start + 1)
        
    print(total_count)

solve()
