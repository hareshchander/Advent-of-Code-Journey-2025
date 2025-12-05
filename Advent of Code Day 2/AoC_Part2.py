def check_pattern(number):
    text = str(number)
    length = len(text)
    limit = (length // 2) + 1
    
    for size in range(1, limit):
        if length % size == 0:
            pattern = text[:size]
            times = length // size
            
            if pattern * times == text:
                return True
                
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
