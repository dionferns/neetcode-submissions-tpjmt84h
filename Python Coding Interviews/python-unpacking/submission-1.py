from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    value1, value2, value3 = triplet
    return value1 + value2 + value3


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    value1, value2, value3 = box_dimensions
    return value1 * value2 * value3
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
