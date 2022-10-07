def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([7,4,9,5,1,6,3,5,1,0,4,5,8,7]))

import numpy as np
data = np.array([7,4,9,5,1,6,3,5,1,0,4,5,8,7])
print(np.sort(data))