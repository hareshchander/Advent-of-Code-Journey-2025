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

    def count_paths(current_node):
        if current_node == 'out':
            return 1
        
        if current_node in memo:
            return memo[current_node]
        
        if current_node not in adj:
            return 0
        
        total_paths = 0
        for neighbor in adj[current_node]:
            total_paths += count_paths(neighbor)
        
        memo[current_node] = total_paths
        return total_paths

    if 'you' in adj:
        result = count_paths('you')
        print(result)
    else:
        print("Error: Starting node 'you' not found in input.")

if __name__ == '__main__':
    solve()
