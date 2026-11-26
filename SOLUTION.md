# Solution

Treat each usable building as a vertex, with unit-cost edges between orthogonal
neighbors. Run BFS from the start and from home. For each shop reachable from
both, minimize the sum of its two distances. Print -1 if no such shop exists;
the statement does not specify an output convention for impossible instances.

Any valid walk visits some shop. Its portions before and after that visit are
at least the corresponding shortest-path distances. Conversely, concatenating
shortest paths through a shop attains that sum. Thus taking the minimum gives
the optimal answer, including routes that revisit buildings.

Both time and memory are O(nm). A blocked border simplifies neighbor traversal.

Build with `cmake -S . -B build && cmake --build build`.
Run local verification with `python3 tests/check.py ./build/code`.
The provided sample-data directory was unavailable in this environment.
