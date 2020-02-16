from __future__ import annotations

from collections import deque
from typing import Deque, Set

from .Item import Item


class Stack:
    """
    Wrapper class for a stack of items, maintained as a deque of Items. Such
    a stack represents a single stack of a truck, from the rear (left) to the
    front (right).
    """
    stack: Deque[Item]
    _set: Set[Item]

    def __init__(self):
        self.stack = deque()
        self._set = set()

    def __contains__(self, item: Item) -> bool:
        """
        Tests if this stack contains the passed-in item. O(1).
        """
        return item in self._set

    def insert_volume(self, at: int) -> float:
        """
        Computes the volume that needs to be moved in order to insert an item at
        the given index. Does not actually change the stack lay-out. O(n), where
        n is the number of stack items.
        """
        return sum(self.stack[idx].volume
                   for idx in range(min(at, len(self.stack))))

    def remove_volume(self, item: Item) -> float:
        """
        Computes the (excess) volume that needs to be moved to remove the
        passed-in item. Does not actually change the stack lay-out. O(n), where
        n is the number of stack items.
        """
        assert item in self
        at = self.stack.index(item)

        return sum(self.stack[idx].volume for idx in range(at))

    def push_front(self, item: Item):
        """
        Places the item in the front of the truck (right). O(1).
        """
        self._set.add(item)
        self.stack.append(item)

    def push_rear(self, item: Item):
        """
        Adds item to the rear of the truck (left). O(1).
        """
        self.stack.appendleft(item)
        self._set.add(item)

    def volume(self) -> float:
        return sum(self.stack[idx].volume
                   for idx in range(len(self.stack)))

    def __str__(self):
        """
        Prints a comma-separated representation of this stack's contents, from
        front (first item) to rear (last). O(n), where n is the number of stack
        items.
        """
        return ",".join(str(item) for item in reversed(self.stack))