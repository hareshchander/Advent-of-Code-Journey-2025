def solve():
    count = 0
    
    with open('sample_input_5.txt', 'r') as f:
        content = f.read().strip()
        
    parts = content.split('\n\n')
    
    range_lines = parts[0].split('\n')
    id_lines = parts[1].split('\n')
    
    ranges = []
    for line in range_lines:
        nums = line.split('-')
        start = int(nums[0])
        end = int(nums[1])
        ranges.append((start, end))
        
    for line in id_lines:
        if not line:
            continue
            
        current_id = int(line)
        is_fresh = False
        
        for r in ranges:
            start = r[0]
            end = r[1]
            
            if current_id >= start and current_id <= end:
                is_fresh = True
                break
                
        if is_fresh:
            count = count + 1
            
    print(count)

solve()
