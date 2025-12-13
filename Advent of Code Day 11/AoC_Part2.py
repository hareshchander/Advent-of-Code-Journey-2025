import sys

sys.setrecursionlimit(100000)

def solve():
    adj = {}
    try:
        with open('sample_input_11.txt', 'r') as f:
            lines = f.read().strip().split('\n')
    except FileNotFoundError:
        print("Error: input.txt not found")
        return

    for line in lines:
        if not line.strip():
            continue
        parts = line.split(':')
        source = parts[0].strip()
        destinations = parts[1].strip().split()
        adj[source] = destinations

    memo = {}

    def count_paths(current_node, visited_dac, visited_fft):
        if current_node == 'dac':
            visited_dac = True
        elif current_node == 'fft':
            visited_fft = True

        if current_node == 'out':
            return 1 if visited_dac and visited_fft else 0
        
        state = (current_node, visited_dac, visited_fft)
        if state in memo:
            return memo[state]
        
        if current_node not in adj:
            return 0
        
        total_paths = 0
        for neighbor in adj[current_node]:
            total_paths += count_paths(neighbor, visited_dac, visited_fft)
        
        memo[state] = total_paths
        return total_paths

    if 'svr' in adj:
        result = count_paths('svr', False, False)
        print(result)
    else:
        print("Error: Starting node 'svr' not found in input.")

if __name__ == '__main__':
    solve()
