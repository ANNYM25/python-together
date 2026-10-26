"""Graphs with BFS and DFS.

Why this exists: knowledge graphs, transaction networks, and layer DAGs are graphs.
Run: python 05-algorithms/graphs_intro.py
"""

from __future__ import annotations

from collections import deque


Graph = dict[str, list[str]]


def bfs(graph: Graph, start: str) -> list[str]:
    seen = {start}
    order = [start]
    q = deque([start])
    while q:
        node = q.popleft()
        for nbr in graph.get(node, []):
            if nbr not in seen:
                seen.add(nbr)
                order.append(nbr)
                q.append(nbr)
    return order


def dfs(graph: Graph, start: str) -> list[str]:
    seen: set[str] = set()
    order: list[str] = []

    def walk(node: str) -> None:
        seen.add(node)
        order.append(node)
        for nbr in graph.get(node, []):
            if nbr not in seen:
                walk(nbr)

    walk(start)
    return order


def demo() -> None:
    graph = {
        "cash": ["bonds", "equity"],
        "bonds": ["ig_credit"],
        "equity": ["climate", "tech"],
        "ig_credit": [],
        "climate": [],
        "tech": [],
    }
    print("bfs", bfs(graph, "cash"))
    print("dfs", dfs(graph, "cash"))


if __name__ == "__main__":
    demo()
