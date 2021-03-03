

path_to_2 = [[1, 0, 0, 0],
             [1, 0, 2, 1],
             [1, 0, 0, 1],
             [1, 1, 1, 1],
             [0, 1, 1, 0],
             [0, 0, 0, 0]]

island_map = [[0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 1, 1, 0, 1, 1, 0],
              [0, 0, 0, 0, 1, 1, 1, 0],
              [1, 1, 0, 0, 0, 0, 0, 0],
              [1, 1, 0, 1, 1, 1, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 1]]
# [[1, 0, 0, 0], [1, 0, 2, 1],[1, 0, 0, 1], [1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 0, 0]]


def bfsArr(arr):
    dist = 0
    queue = []
    dest = []
    visited = []
    rowLen = len(arr)
    colLen = len(arr[0])
    for i in range(len(arr)):  # y
        for j in range(len(arr[i])):  # x
            if arr[i][j] == 0:
                # x,y,dist
                visited.append([i, j, 0])
            elif arr[i][j] == 2:
                dest = [i, j, 0]

    queue.append([0, 0, 0, []])
    next = None
    # next[0] y
    # next[1]   x
    # next[2] distance traveled
    # next[3]   previous nodes explored
    while len(queue) != 0:
        next = queue.pop(0)
        # TODO implement kept array to get to point
        if [next[0], next[1], 0, []] not in visited:
            visited.append([next[0], next[1], 0, []])
            prev = next[3]

            if (next[0]+1 < len(arr)) and arr[next[0]+1][next[1]] != 0:
                if [next[0], next[1]] not in prev:
                    prev.append([next[0], next[1]])
                queue.append([next[0]+1, next[1], next[2]+1, prev])

            if next[1]+1 < len(arr[0]) and arr[next[0]][next[1]+1] != 0:
                if [next[0], next[1]] not in prev:
                    prev.append([next[0], next[1]])
                queue.append([next[0], next[1]+1, next[2]+1, prev])

            if next[0]-1 >= 0 and arr[next[0]-1][next[1]] != 0:
                if [next[0], next[1]] not in prev:
                    prev.append([next[0], next[1]])
                queue.append([next[0]-1, next[1], next[2]+1, prev])

            if next[1]-1 >= 0 and arr[next[0]][next[1]-1] != 0:
                if [next[0], next[1]] not in prev:
                    prev.append([next[0], next[1]])
                queue.append([next[0], next[1]-1, next[2]+1, prev])

    print(next[3])
    return next[2]


def dfs_islands(arr):
    row_len = len(arr)
    col_len = len(arr[0])
    islands = 0
    for i in range(row_len):
        for j in range(col_len):
            if arr[i][j] == 1:
                # for each island tile we check for island, and adjust the array accordingly
                arr = find_island(i, j, arr)
                islands += 1

    return islands


def find_island(r, c, grid):
    row_len = len(grid)
    col_len = len(grid[0])
    # get widths of array
    if r < 0 or r >= row_len or c < 0 or c >= col_len:
        return grid
    # if current tile is island, set to ocean and then check its neighbors
    if grid[r][c] == 1:  # if current tile is island, check nearby tiles for island
        grid[r][c] = 0
        find_island(r+1, c, grid)
        find_island(r-1, c, grid)
        find_island(r, c+1, grid)
        find_island(r, c-1, grid)
        return grid
    else:
        return grid


def dijkstra():
    # Dijkstras search algorithms to find shortest path in graph
    return 6


print(bfsArr(path_to_2))
# lets bfs the 2d array but we can only step on 1's and 0's cannot be walked on

# iterate through 2d array to see how many island there are
print(dfs_islands(island_map))
