from collections import deque

def is_path_possible(maze):
    """
    Checks if a valid path exists from top-left to bottom-right in the maze.
    """
    return shortest_path_with_path(maze)[0]

def shortest_path_length(maze):
    """
    Returns the length of the shortest path from top-left to bottom-right in the maze.
    Returns -1 if no path exists.
    """
    return shortest_path_with_path(maze)[1]

def shortest_path_with_path(maze):
    """
    Helper function that uses BFS to check for a valid path and find the shortest path length and path.
    Returns a tuple: (path_exists: bool, shortest_length: int, path: list of (row, col))
    """
    if not maze or maze[0][0] == 1:
        return (False, -1, [])

    n, m = len(maze), len(maze[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    parent = dict()
    queue = deque()

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Start from (0, 0)
    queue.append((0, 0))
    visited[0][0] = True
    parent[(0, 0)] = None

    while queue:
        row, col = queue.popleft()

        # Check if we reached the end
        if row == n - 1 and col == m - 1:
            # Reconstruct path
            path = []
            current = (row, col)
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return (True, len(path) - 1, path)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < n and 0 <= new_col < m and not visited[new_row][new_col] and maze[new_row][new_col] == 0:
                visited[new_row][new_col] = True
                queue.append((new_row, new_col))
                parent[(new_row, new_col)] = (row, col)

    return (False, -1, [])


# ---------- Example Usage ----------
if __name__ == "__main__":
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]

    has_path = is_path_possible(maze)
    length = shortest_path_length(maze)
    _, _, path = shortest_path_with_path(maze)

    print("Is there a valid path?")
    print(has_path)

    print("\nLength of the shortest path:")
    print(length)

    if has_path:
        print("\nThe actual shortest path (row, col):")
        print(path)
    else:
        print("\nNo path exists.")
