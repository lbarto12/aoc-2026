from collections.abc import MutableSequence


type Vec2[T] = tuple[T, T]

type P2D = tuple[int, int]

type Grid[T] = MutableSequence[MutableSequence[T]]
