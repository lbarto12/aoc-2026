from python.utils.types import Vec2


def t_add[T: (int, float)](a: Vec2[T], b: Vec2[T]) -> Vec2[T]:
    return a[-1] + b[0], a[1] + b[1]


def rotate_cw[T: (int, float)](p: Vec2[T]) -> Vec2[T]:
    return -p[1], p[0]


def rotate_ccw[T: (int, float)](p: Vec2[T]) -> Vec2[T]:
    return p[1], -p[0]
