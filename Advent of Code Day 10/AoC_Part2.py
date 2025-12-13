import re
from fractions import Fraction
import math
import itertools

def rref(matrix):
    if not matrix: return []
    m = len(matrix)
    n = len(matrix[0])
    lead = 0
    for r in range(m):
        if lead >= n:
            return matrix
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == m:
                i = r
                lead += 1
                if lead == n:
                    return matrix
        matrix[i], matrix[r] = matrix[r], matrix[i]
        lv = matrix[r][lead]
        matrix[r] = [mrx / lv for mrx in matrix[r]]
        for i in range(m):
            if i != r:
                lv = matrix[i][lead]
                matrix[i] = [iv - lv * rv for rv, iv in zip(matrix[r], matrix[i])]
        lead += 1
    return matrix

def solve_machine(buttons, targets):
    num_vars = len(buttons)
    num_eqs = len(targets)
    
    matrix = []
    for r in range(num_eqs):
        row = []
        for btn in buttons:
            if r in btn:
                row.append(Fraction(1))
            else:
                row.append(Fraction(0))
        row.append(Fraction(targets[r]))
        matrix.append(row)
        
    matrix = rref(matrix)
    
    pivots = {} 
    for r in range(num_eqs):
        for c in range(num_vars):
            if matrix[r][c] != 0:
                pivots[c] = r
                break
                
    for r in range(num_eqs):
        all_zeros = True
        for c in range(num_vars):
            if matrix[r][c] != 0:
                all_zeros = False
                break
        if all_zeros and matrix[r][-1] != 0:
            return None

    free_vars = [c for c in range(num_vars) if c not in pivots]
    
    min_presses = float('inf')
    
    if not free_vars:
        current_sum = 0
        valid = True
        for c in range(num_vars):
            if c in pivots:
                val = matrix[pivots[c]][-1]
                if val < 0 or val.denominator != 1:
                    valid = False; break
                current_sum += int(val)
        if valid:
            return current_sum
        return None

    # Bounded search for free variables.
    # Since A >= 0 and b >= 0, no variable x_j can exceed max(b)
    limit = max(targets) + 1 if targets else 50
    ranges = [range(limit) for _ in free_vars]
    
    for combo in itertools.product(*ranges):
        current_sum = sum(combo)
        if current_sum >= min_presses:
            continue
            
        valid = True
        
        for c in range(num_vars):
            if c in pivots:
                row_idx = pivots[c]
                val = matrix[row_idx][-1]
                
                for idx, fv in enumerate(free_vars):
                    coeff = matrix[row_idx][fv]
                    val -= coeff * combo[idx]
                
                if val < 0 or val.denominator != 1:
                    valid = False
                    break
                current_sum += int(val)
                if current_sum >= min_presses:
                    valid = False
                    break
        
        if valid:
            if current_sum < min_presses:
                min_presses = current_sum
                
    return min_presses if min_presses != float('inf') else None

def solve():
    try:
        with open('sample_input_10.txt', 'r') as f:
            lines = f.read().strip().split('\n')
    except FileNotFoundError:
        print("Error: input.txt not found")
        return

    total_presses = 0

    for line in lines:
        if not line.strip():
            continue

        target_match = re.search(r'\{([\d,]+)\}', line)
        if not target_match:
            continue
        targets = [int(x) for x in target_match.group(1).split(',')]

        button_matches = re.findall(r'\(([\d,]+)\)', line)
        buttons = []
        for b_str in button_matches:
            indices = set(int(x) for x in b_str.split(','))
            buttons.append(indices)

        result = solve_machine(buttons, targets)
        
        if result is not None:
            total_presses += result
        else:
            print(f"No solution for: {line}")

    print(total_presses)

if __name__ == '__main__':
    solve()
