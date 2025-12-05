def solve():
    total_sum = 0
    
    with open('sample_input_3.txt', 'r') as f:
        content = f.read().strip()
        
    lines = content.split('\n')
    
    for line in lines:
        best_num = 0
        length = len(line)
        
        for i in range(length):
            for j in range(i + 1, length):
                digit1 = line[i]
                digit2 = line[j]
                
                number = int(digit1 + digit2)
                
                if number > best_num:
                    best_num = number
                    
        total_sum = total_sum + best_num
        
    print(total_sum)

solve()
