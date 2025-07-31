from collections import deque

def is_valid(x, y, M, N):
    return 0 <= x < M and 0 <= y < N

def rotate(dx, dy, direction):
    # 0 = forward, 1 = right, 2 = back, 3 = left
    if direction == 0:  # forward
        return dx, dy
    elif direction == 1:  # right (90 degrees clockwise)
        return dy, -dx
    elif direction == 2:  # back (180 degrees)
        return -dx, -dy
    elif direction == 3:  # left (90 degrees counter-clockwise)
        return -dy, dx

def min_moves(grid, source, destination, move_rule):
    M, N = len(grid), len(grid[0])
    visited = [[False for _ in range(N)] for _ in range(M)]
    queue = deque()
    
    sx, sy = source
    dx, dy = destination
    
    queue.append((sx, sy, 0))
    visited[sx][sy] = True

    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == (dx, dy):
            return steps

        for direction in range(4):  # forward, right, back, left
            mx, my = rotate(move_rule[0], move_rule[1], direction)
            nx, ny = x + mx, y + my

            if is_valid(nx, ny, M, N) and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))

    return -1  # If destination not reachable

# -------- Input Section --------
def main():
    M, N = map(int, input().split())
    grid = []
    for _ in range(M):
        grid.append(list(map(int, input().split())))

    sx, sy = map(int, input().split())
    dx, dy = map(int, input().split())
    mx, my = map(int, input().split())

    result = min_moves(grid, (sx, sy), (dx, dy), (mx, my))
    print(result)

# Run the main function
if __name__ == "__main__":
    main()
