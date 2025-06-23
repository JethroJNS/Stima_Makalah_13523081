def solve_gym_puzzle(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Temukan posisi awal (S) dan hitung total titik yang harus dikunjungi
    start_pos = None
    target_positions = set()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start_pos = (i, j)
            if grid[i][j] == '.' or grid[i][j] == 'G':
                target_positions.add((i, j))
    
    if not start_pos:
        return None, 0
    
    target_count = len(target_positions)
    
    # Arah: kiri, kanan, atas, bawah
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    best_path = None
    nodes_visited = 0
    
    def is_valid(x, y, visited):
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] != 'X' and not visited[x][y]
    
    def can_reach_all_targets(x, y, visited, remaining_targets):
        # Buat salinan visited untuk flood fill
        visited_copy = [row[:] for row in visited]
        queue = [(x, y)]
        visited_copy[x][y] = True
        found_targets = set()
        
        while queue:
            cx, cy = queue.pop(0)
            if (cx, cy) in remaining_targets:
                found_targets.add((cx, cy))
                if len(found_targets) == len(remaining_targets):
                    return True
            
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if is_valid(nx, ny, visited_copy):
                    visited_copy[nx][ny] = True
                    queue.append((nx, ny))
        
        return len(found_targets) == len(remaining_targets)
    
    def backtrack(x, y, visited, path, remaining_targets):
        nonlocal best_path, nodes_visited
        nodes_visited += 1
        
        current_char = grid[x][y]
        new_remaining = remaining_targets.copy()
        
        # Jika menginjak target, hapus dari remaining_targets
        if (x, y) in new_remaining:
            new_remaining.remove((x, y))
        
        # Basis: mencapai G dan semua target terpenuhi
        if current_char == 'G' and not new_remaining:
            if best_path is None or len(path) + 1 < len(best_path):
                best_path = path + [(x, y)]
            return
        
        # Prune jika tidak semua target bisa dicapai dari posisi ini
        if not can_reach_all_targets(x, y, visited, new_remaining):
            return
        
        # Tandai sudah dikunjungi
        visited[x][y] = True
        
        # Rekursi: coba semua arah
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited):
                backtrack(nx, ny, [row[:] for row in visited], path + [(x, y)], new_remaining)
        
        # Unmark visited untuk backtracking
        visited[x][y] = False
    
    # Mulai backtracking dari posisi awal
    initial_visited = [[False for _ in range(cols)] for _ in range(rows)]
    backtrack(start_pos[0], start_pos[1], initial_visited, [], target_positions)
    
    return best_path, nodes_visited

def print_solution(grid, path, nodes_visited):
    if not path:
        print("Tidak ada solusi ditemukan")
        print(f"Jumlah node yang dikunjungi: {nodes_visited}")
        return
    
    solution_grid = [list(row) for row in grid]  # Buat salinan grid
    for step, (x, y) in enumerate(path[1:], 1):
        if solution_grid[x][y] not in ['S', 'G']:
            # Format step dengan dua digit, jika step > 99 maka akan menunjukkan tiga digit
            solution_grid[x][y] = f"{step:02d}"
    
    for row in solution_grid:
        print(' '.join(f"{str(c):>2}" for c in row))
    print(f"Jumlah node yang dikunjungi: {nodes_visited}")
    print()

# Puzzle 1
puzzle1 = [
    ['X', 'G', '.'],
    ['.', '.', '.'],
    ['.', 'S', 'X']
]
print("Solusi Puzzle 1:")
path1, nodes1 = solve_gym_puzzle(puzzle1)
print_solution(puzzle1, path1, nodes1)

# Puzzle 2
puzzle2 = [
    ['.', '.', '.', 'G', '.', '.', '.'],
    ['.', 'X', '.', '.', '.', 'X', '.'],
    ['.', '.', '.', 'S', '.', '.', '.']
]
print("Solusi Puzzle 2:")
path2, nodes2 = solve_gym_puzzle(puzzle2)
print_solution(puzzle2, path2, nodes2)

# Puzzle 3
puzzle3 = [
    ['.', '.', 'X', '.', '.', 'G', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', 'X', '.', '.', 'X', '.'],
    ['.', 'X', '.', '.', 'X', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'S', '.', '.', 'X', '.', '.']
]
print("Solusi Puzzle 3:")
path3, nodes3 = solve_gym_puzzle(puzzle3)
print_solution(puzzle3, path3, nodes3)