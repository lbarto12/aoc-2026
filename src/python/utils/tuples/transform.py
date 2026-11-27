def t_add[T: (int, float)](a: tuple[T, T], b: tuple[T, T]) -> tuple[T, T]:
    return a[-1] + b[0], a[1] + b[1]


def rotate_cw[T: (int, float)](p: tuple[T, T]) -> tuple[T, T]:
    return -p[1], p[0]


def rotate_ccw[T: (int, float)](p: tuple[T, T]) -> tuple[T, T]:
    return p[1], -p[0]
