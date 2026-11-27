from collections.abc import Iterable, Iterator


class DisjointSetUnion[T]:
    def __init__(self, items: Iterable[T]):
        self.parent: dict[T, T] = {i: i for i in items}
        self.sizes: dict[T, int] = {i: 1 for i in items}
        self.size: int = len(list(items))

    def find(self, i: T) -> T:
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i: T, j: T):
        if self.find(i) != self.find(j):
            self.parent[a := self.find(i)] = (b := self.find(j))
            self.sizes[b] += self.sizes[a]
            self.sizes[a] = 0
            self.size -= 1

    def len(self, i: T) -> int:
        return self.sizes[self.find(i)]

    def __iter__(self) -> Iterator[T]:
        return list(set(self.find(i) for i in self.parent.keys())).__iter__()

    def __len__(self) -> int:
        return self.size
