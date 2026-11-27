from collections.abc import Generator, Sequence

from src.python.utils.tuples.transform import t_add


def adjacent(pos: tuple[int, int]) -> Generator[tuple[int, int]]:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) == (0, 0):
                continue
            yield (pos[0] + j, pos[1] + i)


def adjacent4(p: tuple[int, int]) -> Generator[tuple[int, int]]:
    for o in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
        yield t_add(p, o)


def in_bounds[T](data: list[list[T]], p: tuple[int, int]) -> bool:
    return 0 <= p[0] < len(data[0]) and 0 <= p[1] < len(data)


def getxy[T](arr: Sequence[Sequence[T]], pos: tuple[int, int]) -> T:
    return arr[pos[1]][pos[0]]


def setxy[T](arr: list[list[T]], pos: tuple[int, int], val: T):
    arr[pos[1]][pos[0]] = val


def count_adjacent[T](
    arr: list[list[T]], pos: tuple[int, int], targets: list[T]
) -> int:
    return sum(arr[y][x] in targets for x, y in adjacent(pos))


def count_adjacent4[T](
    arr: list[list[T]], pos: tuple[int, int], targets: list[T]
) -> int:
    return sum(arr[y][x] in targets for x, y in adjacent4(pos))
