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

Build with `make`.
Run local verification with `python3 tests/check.py ./code`.
The provided sample-data directory was unavailable in this environment.

## Verification and judge results

Local verification passed the statement sample, explicit edge cases, randomized
comparisons with a BFS tracking umbrella ownership, and a 1000 by 1000 open grid.
Both the original CMake build and the final direct Make build succeeded locally.

All five allowed submissions returned `compile_error` with score 0 and no
compiler diagnostics or test groups:

| Submission | Build | Repository transport |
| --- | --- | --- |
| 879572 | CMake, C++17 | HTTPS |
| 879575 | CMake, C++17 | SSH on port 443 |
| 879580 | GNUmakefile, C++11 | HTTPS |
| 879582 | GNUmakefile, C++11 | Standard SSH |
| 879586 | Makefile, C++11 | HTTPS |

The judge-side failure remains unresolved. No submissions were aborted, and no
additional submissions were made after reaching the five-attempt limit.
