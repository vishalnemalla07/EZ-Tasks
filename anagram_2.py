def find_path(matrix, x_dest, y_dest):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    visited[0][0] = True

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 1 and not visited[x][y]

    def dfs(x, y):
        if x == x_dest and y == y_dest:
            return True
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for nx, ny in neighbors:
            if is_valid(nx, ny):
                visited[nx][ny] = True
                if dfs(nx, ny):
                    return True
        return False

    return dfs(0, 0)

if __name__ == "__main__":
    rows = int(input())
    cols = int(input())
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))
    x_dest = int(input())
    y_dest = int(input())

    if find_path(matrix, x_dest, y_dest):
        print("path found")
    else:
        print("path not found")
