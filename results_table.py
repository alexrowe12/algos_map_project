"""Run Dijkstra on several source/target pairs to populate the report's
results table."""

from shortest_path import dijkstra
from graph import graph

PAIRS = [
    ("Los Angeles", "New York City"),
    ("Seattle", "Miami"),
    ("San Francisco", "Boston"),
    ("Los Angeles", "Boston"),
    ("Seattle", "Jacksonville"),
    ("San Francisco", "Washington, DC"),
]

print(f"{'Source':<16} {'Target':<16} {'Distance':>9}  Path")
print("-" * 100)
for src, dst in PAIRS:
    distance, path = dijkstra(graph, src, dst)
    print(f"{src:<16} {dst:<16} {distance:>9}  {' -> '.join(path)}")
