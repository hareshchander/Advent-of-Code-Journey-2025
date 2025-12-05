def check_pattern(number):
    text = str(number)
    length = len(text)
    
    if length % 2 != 0:
        return False
        
    half_size = length // 2
    first_part = text[:half_size]
    second_part = text[half_size:]
    
    if first_part == second_part:
        return True
    else:
        return False

def solve():
    total_sum = 0
    
    with open('sample_input_2.txt', 'r') as f:
        data = f.read().strip()
        
    ranges = data.split(',')
    
    for item in ranges:
        parts = item.split('-')
        start = int(parts[0])
        end = int(parts[1])
        
        for num in range(start, end + 1):
            if check_pattern(num) == True:
                total_sum = total_sum + num
                
    print(total_sum)

solve()
