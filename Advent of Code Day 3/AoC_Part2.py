def solve():
    total_sum = 0
    
    with open('sample_input_3.txt', 'r') as f:
        data = f.read().strip()
        
    lines = data.split('\n')
    
    for line in lines:
        if not line:
            continue
            
        current_index = 0
        best_string = ""
        needed = 12
        
        for step in range(12):
            length = len(line)
            limit = length - (needed - 1)
            
            highest_digit = -1
            chosen_index = -1
            
            for i in range(current_index, limit):
                digit = int(line[i])
                if digit > highest_digit:
                    highest_digit = digit
                    chosen_index = i
            
            best_string = best_string + str(highest_digit)
            current_index = chosen_index + 1
            needed = needed - 1
            
        total_sum = total_sum + int(best_string)
        
    print(total_sum)

solve()
