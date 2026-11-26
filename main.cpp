#include <algorithm>
#include <iostream>
#include <vector>

std::vector<int> distances(const std::vector<int>& grid, int source, int stride) {
    std::vector<int> distance(grid.size(), -1);
    if (source == -1) return distance;

    std::vector<int> queue;
    queue.reserve(grid.size());
    queue.push_back(source);
    distance[source] = 0;
    const int offsets[] = {-stride, stride, -1, 1};
    for (std::size_t head = 0; head < queue.size(); ++head) {
        const int current = queue[head];
        for (int offset : offsets) {
            const int next = current + offset;
            if (grid[next] != 1 && distance[next] == -1) {
                distance[next] = distance[current] + 1;
                queue.push_back(next);
            }
        }
    }
    return distance;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int width, height;
    if (!(std::cin >> width >> height)) return 0;
    const int stride = width + 2;
    // A blocked border makes every neighbor of a traversable cell a valid index.
    std::vector<int> grid((height + 2) * stride, 1);
    std::vector<int> shops;
    int start = -1, home = -1;
    for (int row = 1; row <= height; ++row) {
        for (int col = 1; col <= width; ++col) {
            const int cell = row * stride + col;
            std::cin >> grid[cell];
            if (grid[cell] == 2) start = cell;
            if (grid[cell] == 3) home = cell;
            if (grid[cell] == 4) shops.push_back(cell);
        }
    }

    const auto from_start = distances(grid, start, stride);
    const auto from_home = distances(grid, home, stride);
    int answer = -1;
    for (int shop : shops) {
        if (from_start[shop] == -1 || from_home[shop] == -1) continue;
        const int candidate = from_start[shop] + from_home[shop];
        if (answer == -1 || candidate < answer) answer = candidate;
    }
    std::cout << answer << '\n';
}
