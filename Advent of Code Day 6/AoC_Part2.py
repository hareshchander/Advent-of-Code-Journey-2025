def calculate_problem(cols):
    numbers = []
    operator = ""
    
    for col in cols:
        last_char = col[-1]
        
        if last_char == "+" or last_char == "*":
            operator = last_char
            
        number_text = col[:-1]
        clean_text = number_text.replace(" ", "")
        
        if clean_text != "":
            numbers.append(int(clean_text))
            
    result = numbers[0]
    
    if operator == "+":
        for i in range(1, len(numbers)):
            result = result + numbers[i]
    elif operator == "*":
        for i in range(1, len(numbers)):
            result = result * numbers[i]
            
    return result

def solve():
    grand_total = 0
    
    with open('sample_input_6.txt', 'r') as f:
        lines = f.read().splitlines()
        
    if not lines:
        print(0)
        return

    max_len = 0
    for line in lines:
        if len(line) > max_len:
            max_len = len(line)
            
    padded_lines = []
    for line in lines:
        padded_lines.append(line.ljust(max_len))
        
    current_problem_cols = []
    
    for x in range(max_len):
        col_str = ""
        for line in padded_lines:
            col_str = col_str + line[x]
            
        if col_str.strip() == "":
            if len(current_problem_cols) > 0:
                grand_total = grand_total + calculate_problem(current_problem_cols)
                current_problem_cols = []
        else:
            current_problem_cols.append(col_str)
            
    if len(current_problem_cols) > 0:
        grand_total = grand_total + calculate_problem(current_problem_cols)
        
    print(grand_total)

solve()
