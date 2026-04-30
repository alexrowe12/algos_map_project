"""Weighted undirected graph of US cities used for the shortest-path task.

Edges represent roads; weights approximate relative driving distances.
The structure is an adjacency list (dict of dicts): graph[u][v] = weight.
"""

graph = {
    "Seattle":        {"San Francisco": 8, "Boise": 5, "Fargo": 14},
    "San Francisco":  {"Seattle": 8, "Los Angeles": 4, "Boise": 8},
    "Los Angeles":    {"San Francisco": 4, "Las Vegas": 2, "Phoenix": 3},
    "Boise":          {"Seattle": 5, "Salt Lake": 3, "Billings": 6, "San Francisco": 8},
    "Billings":       {"Boise": 6, "Fargo": 6, "Denver": 6},
    "Salt Lake":      {"Boise": 3, "Phoenix": 8, "Las Vegas": 4, "Denver": 5},
    "Las Vegas":      {"Los Angeles": 2, "Salt Lake": 4},
    "Phoenix":        {"Los Angeles": 3, "El Paso": 4, "Amarillo": 7, "Salt Lake": 8},
    "Denver":         {"Salt Lake": 5, "Omaha": 5, "Amarillo": 4,
                       "Billings": 6, "Fargo": 9},
    "Fargo":          {"Seattle": 14, "Billings": 6, "Minneapolis": 2,
                       "Denver": 9},
    "Minneapolis":    {"Fargo": 2, "Milwaukee": 3, "Omaha": 4},
    "Milwaukee":      {"Minneapolis": 3, "Chicago": 1, "Omaha": 5},
    "Chicago":        {"Milwaukee": 1, "St. Louis": 3, "Pittsburgh": 5},
    "Omaha":          {"Milwaukee": 5, "Minneapolis": 4, "Denver": 5,
                       "St. Louis": 5, "Amarillo": 7, "Little Rock": 6},
    "Amarillo":       {"Phoenix": 7, "Denver": 4, "Dallas": 3,
                       "El Paso": 4, "Omaha": 7},
    "El Paso":        {"Phoenix": 4, "Dallas": 7, "Houston": 8, "Amarillo": 4},
    "Dallas":         {"Amarillo": 3, "El Paso": 7, "Little Rock": 3,
                       "Houston": 2},
    "Houston":        {"Dallas": 2, "El Paso": 8, "New Orleans": 3},
    "New Orleans":    {"Houston": 3, "Little Rock": 4, "Jacksonville": 6},
    "Little Rock":    {"Omaha": 6, "Dallas": 3, "St. Louis": 3,
                       "New Orleans": 4, "Atlanta": 5},
    "St. Louis":      {"Chicago": 3, "Omaha": 5, "Little Rock": 3,
                       "Nashville": 3},
    "Nashville":      {"St. Louis": 3, "Atlanta": 2, "Washington, DC": 7},
    "Atlanta":        {"Little Rock": 5, "Nashville": 2, "Jacksonville": 3},
    "Jacksonville":   {"Atlanta": 3, "New Orleans": 6, "Raleigh": 5,
                       "Miami": 4},
    "Miami":          {"Jacksonville": 4},
    "Raleigh":        {"Jacksonville": 5, "Washington, DC": 3},
    "Pittsburgh":     {"Chicago": 5, "Washington, DC": 2,
                       "New York City": 4},
    "Washington, DC": {"Pittsburgh": 2, "Nashville": 7, "Raleigh": 3,
                       "New York City": 2},
    "New York City":  {"Pittsburgh": 4, "Washington, DC": 2, "Boston": 2},
    "Boston":         {"New York City": 2},
}


def validate_symmetric(g):
    """Return a list of asymmetries: edges present in one direction only or
    with mismatched weights. Empty list means the graph is well-formed."""
    issues = []
    for u, neighbors in g.items():
        for v, w in neighbors.items():
            if v not in g:
                issues.append(f"{u} -> {v} but {v} is not a node")
                continue
            if u not in g[v]:
                issues.append(f"{u} -> {v} ({w}) has no reverse edge")
            elif g[v][u] != w:
                issues.append(f"{u}-{v} weight mismatch: {w} vs {g[v][u]}")
    return issues


if __name__ == "__main__":
    problems = validate_symmetric(graph)
    if problems:
        print(f"Found {len(problems)} issue(s):")
        for p in problems:
            print(f"  - {p}")
    else:
        print(f"Graph OK: {len(graph)} nodes, "
              f"{sum(len(n) for n in graph.values()) // 2} undirected edges.")
