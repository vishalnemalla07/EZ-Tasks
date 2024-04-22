def is_valid(matrix, visited, x, y):
    rows = len(matrix)
    cols = len(matrix[0])
    return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 1 and not visited[x][y]

def find_path(matrix, visited, x, y):
    if (x, y) == (0, 0):
        return True

    visited[x][y] = True

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid(matrix, visited, new_x, new_y):
            if find_path(matrix, visited, new_x, new_y):
                return True

    return False

def main():
    rows = int(input())
    cols = int(input())
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    x = int(input())
    y = int(input())

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    if find_path(matrix, visited, x, y):
        print("path found")
    else:
        print("path not found")

if __name__ == "__main__":
    main()
