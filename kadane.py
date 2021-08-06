import time

import numpy as np
import math
import tracemalloc

#KADANE ALGORITHM
def kadane_algorithm(a, n):
    M = 0
    t = 0
    x1 = 0
    x2 = 0
    i = 1

    for j in range(0, n):
        t = t + a[j]

        if t < 0:
            t = 0
            i = j+1

        elif t > M:
            M = t
            x1 = i
            x2 = j

    return M, x1, x2

#ARRAY
a = np.random.randint(-10, 10, 10)
a = np.array(a)
#TRACK MEMORY
tracemalloc.start()
#TRACK TIME
begin = time.time()
max_sum_subarray_kadane = kadane_algorithm(a, len(a))
#STOP TRACKING TIME
end = time.time()
#STOP TRACKING MEMORY
snapshot= tracemalloc.take_snapshot()
for stat in snapshot.statistics("lineno"):
    print("stat kadane")
    print(stat)
    print(stat.traceback.format())
#PRINT MEMORY
print("\nTraced Memory (Current, Peak): ", tracemalloc.get_traced_memory())
#PRINT TIME
print("Time:")
print(end-begin)
