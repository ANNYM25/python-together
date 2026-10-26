"""Stack and queue.

Why this exists: DFS uses a stack; BFS uses a queue; undo uses a stack.
Run: python 05-algorithms/stack_queue.py
"""

from __future__ import annotations

from collections import deque


def demo() -> None:
    stack: list[str] = []
    stack.append("open file")
    stack.append("edit")
    print("undo", stack.pop())
    print("stack now", stack)

    q: deque[str] = deque()
    q.append("client A")
    q.append("client B")
    print("serve", q.popleft())
    print("queue now", list(q))


if __name__ == "__main__":
    demo()
