from array import array
from ctypes import Array
from typing import Tuple


def binary_search(numbers: Array, value: int) -> Tuple[bool, int]:
    start: int = 0
    end: int = len(numbers) - 1

    while start <= end:
        middle: int = (start + end) // 2
        if value == numbers[middle]:
            return True, middle
        if value > numbers[middle]:
            start += 1
        if value < numbers[middle]:
            end -= 1

    return False, -1


ints = array('I', [1, 5, 6, 7, 10, 26, 29, 40])

result = binary_search(ints, 7)
print(result)