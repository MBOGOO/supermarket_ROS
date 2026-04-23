import heapq

# Simple grid supermarket map (0 = free, 1 = obstacle)
grid = [
    [0,0,0,1,0,0],
    [0,1,0,1,0,0],
    [0,1,0,0,0,1],
    [0,0,0,1,0,0],
    [1,0,0,0,0,0]
]

start = (0,0)
goal = (4,5)

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            break

        x, y = current
        moves = [(1,0),(-1,0),(0,1),(0,-1)]

        for dx, dy in moves:
            nx, ny = x+dx, y+dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == 1:
                    continue

                new_cost = cost[current] + 1

                if (nx,ny) not in cost or new_cost < cost[(nx,ny)]:
                    cost[(nx,ny)] = new_cost
                    priority = new_cost + heuristic(goal, (nx,ny))
                    heapq.heappush(open_list, (priority, (nx,ny)))
                    came_from[(nx,ny)] = current

    # reconstruct path
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = came_from.get(node, start)
    path.append(start)
    path.reverse()

    return path

print("A* Path:", astar(start, goal))
