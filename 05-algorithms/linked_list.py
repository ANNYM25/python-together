"""Singly linked list.

Why this exists: it is the simplest structure where 'next' is explicit.
Run: python 05-algorithms/linked_list.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def prepend(self, value: int) -> None:
        self.head = Node(value, self.head)

    def to_list(self) -> list[int]:
        out: list[int] = []
        node = self.head
        while node is not None:
            out.append(node.value)
            node = node.next
        return out


def demo() -> None:
    chain = LinkedList()
    for value in (3, 2, 1):
        chain.prepend(value)
    print(chain.to_list())


if __name__ == "__main__":
    demo()
