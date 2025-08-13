def flood_fill(grid, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return
    h = int(grid[r][c])
    if h == 0:
        return
    grid[r] = grid[r][:c] + '0' + grid[r][c+1:]
    if r > 0 and int(grid[r-1][c]) <= h:
        flood_fill(grid, r-1, c)
    if r < len(grid)-1 and int(grid[r+1][c]) <= h:
        flood_fill(grid, r+1, c)
    if c > 0 and int(grid[r][c-1]) <= h:
        flood_fill(grid, r, c-1)
    if c < len(grid[0])-1 and int(grid[r][c+1]) <= h:
        flood_fill(grid, r, c+1)

def print_grid(grid, idx=0):
    if idx == len(grid):
        return
    print(grid[idx])
    print_grid(grid, idx+1)

def valid_input(R, C, grid, sr, sc):

    if not (1 <= R <= 9 and 1 <= C <= 9):
        print("Error: Rows and columns must be between 1 and 9")
        return False

    if len(grid) != R or any(len(row) != C for row in grid):
        print("Error: Map size does not match rows and columns")
        return False

    if not (0 <= sr < R and 0 <= sc < C):
        print("Error: Start coordinates are out of grid bounds")
        return False
    return True

data = input(" *** Water Flow ***\nInput rows,cols/data1,data2,.../start_row,start_col : ").strip()
try:
    size_part, map_part, start_part = data.split('/')
    R, C = map(int, size_part.split(','))
    grid = map_part.split(',')
    sr, sc = map(int, start_part.split(','))
except:
    print("Error: Invalid input format")
    exit()

if valid_input(R, C, grid, sr, sc):
    flood_fill(grid, sr, sc)
    print_grid(grid)
