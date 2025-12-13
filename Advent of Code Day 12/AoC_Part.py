import sys
import os

sys.setrecursionlimit(2000)

def parse_input(filename):
    content = None
    
    # List of candidate filenames to try
    candidates = [filename]
    if not filename.endswith('.txt'):
        candidates.append(filename + '.txt')
    else:
        candidates.append(filename[:-4])
        
    for cand in candidates:
        if os.path.exists(cand):
            try:
                with open(cand, 'r') as f:
                    content = f.read().strip()
                print(f"Successfully loaded: {cand}")
                break
            except Exception as e:
                print(f"Error reading {cand}: {e}")
    
    if content is None:
        print(f"Error: Could not find file '{filename}' or variations {candidates}.")
        print(f"Current working directory: {os.getcwd()}")
        return None, None

    blocks = content.replace('\r\n', '\n').split('\n\n')
    shapes = {}
    queries = []

    for block in blocks:
        lines = [line.strip() for line in block.split('\n') if line.strip()]
        if not lines:
            continue
            
        header = lines[0]
        if ':' not in header:
            continue

        id_part = header.split(':')[0].strip()
        
        if 'x' in id_part:
            for line in lines:
                if ':' not in line: continue
                parts = line.split(':')
                dims_part = parts[0].strip()
                if 'x' not in dims_part: continue
                
                w_str, h_str = dims_part.split('x')
                w, h = int(w_str), int(h_str)
                
                counts_part = parts[1].strip()
                if not counts_part: continue 
                
                counts = list(map(int, counts_part.split()))
                queries.append({'w': w, 'h': h, 'counts': counts})
        else:
            shape_id = int(id_part)
            grid_lines = []
            
            parts = header.split(':')
            first_line_content = parts[1].strip()
            if first_line_content:
                grid_lines.append(first_line_content)
                
            grid_lines.extend(lines[1:])
            
            coords = []
            for r, line in enumerate(grid_lines):
                for c, char in enumerate(line):
                    if char == '#':
                        coords.append((r, c))
            shapes[shape_id] = coords
            
    return shapes, queries

def normalize_shape(coords):
    if not coords:
        return frozenset()
    min_r = min(r for r, c in coords)
    min_c = min(c for r, c in coords)
    return frozenset((r - min_r, c - min_c) for r, c in coords)

def get_variations(base_coords):
    variations = set()
    
    current = base_coords
    for _ in range(2):
        for _ in range(4):
            variations.add(normalize_shape(current))
            current = [(c, -r) for r, c in current]
        current = [(r, -c) for r, c in current]
        
    return list(variations)

def generate_placements(w, h, variation_coords):
    placements = []
    
    if not variation_coords:
        return []
        
    max_r = max(r for r, c in variation_coords)
    max_c = max(c for r, c in variation_coords)
    
    for r in range(h - max_r):
        for c in range(w - max_c):
            mask = 0
            for vr, vc in variation_coords:
                bit_idx = (r + vr) * w + (c + vc)
                mask |= (1 << bit_idx)
            placements.append(mask)
            
    return placements

def solve_region(w, h, counts, shapes, region_idx):
    pieces = []
    for shape_id, count in enumerate(counts):
        if count > 0:
            if shape_id not in shapes:
                print(f"  [Error] Shape ID {shape_id} not found definitions.")
                return False
            for _ in range(count):
                pieces.append(shape_id)
    
    total_area = sum(len(shapes[sid]) for sid in pieces)
    if total_area > w * h:
        print(f"Region {region_idx}: [FAIL] Area too small ({total_area} > {w*h})")
        return False

    pieces.sort(key=lambda sid: len(shapes[sid]), reverse=True)
    
    piece_masks = {}
    unique_ids = set(pieces)
    
    for sid in unique_ids:
        base_coords = shapes[sid]
        variations = get_variations(base_coords)
        
        all_masks = []
        for var in variations:
            masks = generate_placements(w, h, var)
            if masks:
                all_masks.extend(masks)
        
        piece_masks[sid] = sorted(list(set(all_masks)), reverse=True)
        
        if not piece_masks[sid]:
             print(f"Region {region_idx}: [FAIL] Shape {sid} cannot fit in {w}x{h}")
             return False

    def backtrack_optimized(idx, current_mask, last_mask_idx):
        if idx == len(pieces):
            return True
        
        sid = pieces[idx]
        possible_masks = piece_masks[sid]
        
        start_i = 0
        if idx > 0 and pieces[idx] == pieces[idx-1]:
            start_i = last_mask_idx + 1
            
        for i in range(start_i, len(possible_masks)):
            p_mask = possible_masks[i]
            if (current_mask & p_mask) == 0:
                if backtrack_optimized(idx + 1, current_mask | p_mask, i):
                    return True
        return False

    success = backtrack_optimized(0, 0, -1)
    if success:
        print(f"Region {region_idx}: [PASS] Fits.")
    else:
        print(f"Region {region_idx}: [FAIL] Cannot pack.")
        
    return success

def solve():
    print("Parsing input...")
    # This will now try 'sample_input_12', 'sample_input_12.txt', etc.
    shapes, queries = parse_input('sample_input_12')
    
    if shapes is None:
        return

    print(f"Loaded {len(shapes)} shapes and {len(queries)} regions.")

    valid_regions = 0
    for i, q in enumerate(queries):
        w, h, counts = q['w'], q['h'], q['counts']
        if solve_region(w, h, counts, shapes, i):
            valid_regions += 1
            
    print(f"\nTotal Valid Regions: {valid_regions}")

if __name__ == '__main__':
    solve()
