from collections.abc import Generator, Iterable

from python.utils.tuples.transform import t_add
from python.utils.types import P2D, Grid


def adjacent(pos: P2D) -> Generator[tuple[int, int]]:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) == (0, 0):
                continue
            yield (pos[0] + j, pos[1] + i)


def adjacent4(p: P2D) -> Generator[P2D]:
    for o in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
        yield t_add(p, o)


def in_bounds[T](data: Grid[T], p: P2D) -> bool:
    return 0 <= p[0] < len(data[0]) and 0 <= p[1] < len(data)


def getxy[T](arr: Grid[T], pos: P2D) -> T:
    return arr[pos[1]][pos[0]]


def setxy[T](arr: Grid[T], pos: P2D, val: T):
    arr[pos[1]][pos[0]] = val


def count_adjacent[T](arr: Grid[T], pos: P2D, targets: Iterable[T]) -> int:
    return sum(arr[y][x] in targets for x, y in adjacent(pos))


def count_adjacent4[T](arr: Grid[T], pos: P2D, targets: Iterable[T]) -> int:
    return sum(arr[y][x] in targets for x, y in adjacent4(pos))
