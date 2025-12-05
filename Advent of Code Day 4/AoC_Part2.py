grid = []
with open("sample_input_4.txt") as f:
    for line in f:
        line = line.strip()
        if line != "":
            grid.append(list(line))

rows = len(grid)
cols = len(grid[0])

directions = [
    (-1,-1), (-1,0), (-1,1),
    (0,-1),          (0,1),
    (1,-1),  (1,0),  (1,1)
]

total_removed = 0

while True:
    to_remove = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                adj = 0
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            adj += 1
                if adj < 4:
                    to_remove.append((r, c))

    if not to_remove:
        break

    for r, c in to_remove:
        grid[r][c] = '.'
        total_removed += 1

print(total_removed)
