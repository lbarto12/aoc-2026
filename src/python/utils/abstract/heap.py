from abc import ABC, abstractmethod

from python.utils.protocols import Comparable


class Heap[T: Comparable](ABC):
    items: list[T]

    @abstractmethod
    def push(self, item: T) -> T: ...

    def top(self) -> T:
        if not self.items:
            raise IndexError("top() called on empty heap")
        return self.items[0]

    @abstractmethod
    def pop(self) -> T: ...

    def __len__(self) -> int:
        return len(self.items)
