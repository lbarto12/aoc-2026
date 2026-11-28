from collections.abc import Iterable
import heapq
from typing import override

from python.utils.abstract.heap import Heap
from python.utils.protocols import Comparable


class MinHeap[T: Comparable](Heap[T]):
    def __init__(self, items: Iterable[T] | None = None) -> None:
        if items is None:
            items = []
        self.items: list[T] = list(items)
        heapq.heapify(self.items)

    @override
    def push(self, item: T) -> T:
        heapq.heappush(self.items, item)
        return item

    @override
    def pop(self) -> T:
        if not self.items:
            raise IndexError("pop() called on empty heap")
        return heapq.heappop(self.items)


class MaxHeap[T: Comparable](Heap[T]):
    def __init__(self, items: Iterable[T] | None = None) -> None:
        if items is None:
            items = []
        self.items: list[T] = list(items)
        heapq.heapify_max(self.items)

    @override
    def push(self, item: T) -> T:
        heapq.heappush_max(self.items, item)
        return item

    @override
    def pop(self) -> T:
        if not self.items:
            raise IndexError("pop() called on empty heap")
        return heapq.heappop_max(self.items)
