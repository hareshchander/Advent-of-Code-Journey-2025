import re
from collections import deque

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


        target_match = re.search(r'\[([.#]+)\]', line)
        if not target_match:
            continue
        
        target_str = target_match.group(1)
        
        target_mask = 0
        for i, char in enumerate(target_str):
            if char == '#':
                target_mask |= (1 << i)


        button_matches = re.findall(r'\(([\d,]+)\)', line)
        
        buttons = []
        for b_str in button_matches:
            b_mask = 0
            # Split "1,3" into [1, 3]
            indices = [int(x) for x in b_str.split(',')]
            for idx in indices:
                b_mask |= (1 << idx)
            buttons.append(b_mask)


        queue = deque([(0, 0)])
        

        visited = {0}
        found = False
        
        while queue:
            current_state, steps = queue.popleft()
            

            if current_state == target_mask:
                total_presses += steps
                found = True
                break
            

            for button in buttons:
                # XOR (^) toggles the bits
                next_state = current_state ^ button
                
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, steps + 1))
        
        if not found:
            print(f"Warning: No solution found for machine: {line}")

    print(total_presses)

if __name__ == '__main__':
    solve()
