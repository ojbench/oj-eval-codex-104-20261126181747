"""Compare the solution with BFS over (position, umbrella purchased) states."""
import collections
import random
import subprocess
import sys


def reference(grid, width, height):
    start = grid.index(2)
    queue = collections.deque([(start, False, 0)])
    seen = {(start, False)}
    while queue:
        cell, bought, distance = queue.popleft()
        if grid[cell] == 3 and bought:
            return distance
        row, col = divmod(cell, width)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = row + dr, col + dc
            if not (0 <= nr < height and 0 <= nc < width):
                continue
            nxt = nr * width + nc
            state = (nxt, bought or grid[nxt] == 4)
            if grid[nxt] != 1 and state not in seen:
                seen.add(state)
                queue.append((*state, distance + 1))
    return -1


def check(grid, width, height, expected=None):
    data = f"{width} {height}\n" + " ".join(map(str, grid)) + "\n"
    result = subprocess.run([sys.argv[1]], input=data, text=True,
                            capture_output=True, check=True)
    if expected is None:
        expected = reference(grid, width, height)
    assert int(result.stdout) == expected, (data, expected, result.stdout)


check([4, 1, 0, 0, 0, 0, 1, 0,
       0, 0, 0, 1, 0, 1, 0, 0,
       0, 2, 1, 1, 3, 0, 4, 0,
       0, 0, 0, 4, 1, 1, 1, 0], 8, 4, 11)
check([2, 3, 4], 3, 1, 3)
check([2, 1, 4, 3], 1, 4, -1)
check([2, 0, 3], 3, 1, -1)
rng = random.Random(104)
for _ in range(1000):
    width, height = rng.randint(1, 10), rng.randint(1, 10)
    if width * height < 3:
        continue
    grid = rng.choices([0, 1, 4], weights=[6, 3, 1], k=width * height)
    start, home = rng.sample(range(len(grid)), 2)
    grid[start], grid[home] = 2, 3
    check(grid, width, height)
grid = [0] * 1_000_000
grid[0], grid[-1], grid[999] = 2, 3, 4
check(grid, 1000, 1000, 1998)
print("Sample, edge cases, randomized comparisons, and maximum grid passed.")
