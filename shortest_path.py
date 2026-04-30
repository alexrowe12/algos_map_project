"""Dijkstra's shortest-path algorithm on the US cities graph.

Uses a binary min-heap (heapq) as the priority queue, giving an overall
time complexity of O((V + E) log V) for a graph with V nodes and E edges.
"""

import heapq
from graph import graph


def dijkstra(g, source, target):
    """Return (total_distance, path) for the shortest route source -> target.

    Standard lazy-deletion variant: stale heap entries are skipped when popped
    rather than decreased in place, which keeps the implementation simple
    while preserving the O((V + E) log V) bound.
    """
    distances = {node: float("inf") for node in g}
    previous = {node: None for node in g}
    distances[source] = 0

    # Heap entries: (tentative_distance, node)
    heap = [(0, source)]

    while heap:
        dist_u, u = heapq.heappop(heap)

        # Skip stale entries left over from an earlier, longer path to u.
        if dist_u > distances[u]:
            continue

        # Early exit: once target is finalised, no shorter path can exist.
        if u == target:
            break

        for v, weight in g[u].items():
            alt = dist_u + weight
            if alt < distances[v]:
                distances[v] = alt
                previous[v] = u
                heapq.heappush(heap, (alt, v))

    # Reconstruct path by walking the predecessor chain from target back.
    if distances[target] == float("inf"):
        return float("inf"), []

    path = []
    node = target
    while node is not None:
        path.append(node)
        node = previous[node]
    path.reverse()

    return distances[target], path


def format_path(distance, path):
    if not path:
        return "No path found."
    arrow = " -> "
    return f"Distance: {distance}\nPath ({len(path)} cities): {arrow.join(path)}"


if __name__ == "__main__":
    source = "Los Angeles"
    target = "New York City"

    distance, path = dijkstra(graph, source, target)
    print(f"Shortest path from {source} to {target}")
    print("-" * 60)
    print(format_path(distance, path))

    # Show the per-leg breakdown for the report.
    if path:
        print("\nLeg breakdown:")
        total = 0
        for a, b in zip(path, path[1:]):
            w = graph[a][b]
            total += w
            print(f"  {a:<16} -> {b:<16} {w:>3}   (cumulative {total})")
