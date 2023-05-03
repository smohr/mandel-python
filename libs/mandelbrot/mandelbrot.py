import numpy as np
from dataclasses import dataclass
from io import BytesIO

characters = [' ', '.', '+', '=', '?', '#', ':', '*']

x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5

@dataclass
class MandelSet:
    result: str

def mandelbrot_set(c: complex, max_iter: int) -> int:
    z = 0j
    n = 0
    while abs(z) < 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n

def mandelbrot_set_numpy(c: np.ndarray, max_iter: int) -> np.ndarray:
    z = np.zeros_like(c, dtype=np.complex128)
    result = np.zeros_like(c, dtype=int)
    mask = np.full_like(c, True, dtype=bool)

    for n in range(max_iter):
        z[mask] = z[mask] * z[mask] + c[mask]
        mask = np.abs(z) < 2
        result[mask] = n

    return result

def mandel(max_iter: int, height: int, width:int):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    x, y = np.meshgrid(x, y)
    c = x + 1j * y

    result = mandelbrot_set_numpy(c, max_iter)

    return result

def mandel_ascii(max_iter: int, height: int, width:int) -> MandelSet:
    def pixel_character(n: int) -> str:
        return characters[min(n // 10, len(characters) - 1)]

    result = mandel(max_iter, height, width)

    result_str = ''.join(
        ''.join(
            pixel_character(result[i, j])
            for j in range(width)
        ) + '\n'
        for i in range(height)
    )

    return MandelSet(result_str)
