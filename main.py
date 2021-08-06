import numpy as np
import math

#KADANE
def kadane_algorithm(a, n):
    m = 0
    t = 0
    x1 = 0
    x2 = 0
    i = 0

    for j in range(0, n):
        t = t + a[j]

        if t < 0:
            t = 0
            i = j+1

        elif t > m:
            m = t
            x1 = i
            x2 = j

    return m, x1, x2

#DAC - FIND MAX CROSS SUBARRAY
def find_max_crossing_subarray(a, low, mid, high):
    max_sum = 0
    left_sum = -math.inf
    max_left = 0
    for i in range(mid, low - 1, -1):
        max_sum = max_sum + a[i]
        if max_sum > left_sum:
            left_sum = max_sum
            max_left = i

    max_sum = 0
    right_sum = -math.inf
    max_right = 0
    for j in range(mid + 1, high + 1):
        max_sum = max_sum + a[j]
        if max_sum > right_sum:
            right_sum = max_sum
            max_right = j

    return max_left, max_right, (left_sum + right_sum)

#DAC - FIND MAX SUBARRAY
def find_maximum_subarray(a, low, high):
    if high == low:
        return low, high, a[low]
    else:
        mid = int((low + high) / 2)
        (left_low, left_high, left_sum) = find_maximum_subarray(a, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(a, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(a, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def divide_and_conquer(a, low, high):
    high = high - 1
    return find_maximum_subarray(a, low, high)

#GENERATE ARRAT
a = np.random.randint(-1000, 1000, 1000)
a = np.array(a)

max_sum_subarray_dac = divide_and_conquer(a, 0, len(a))
max_sum_subarray_kadane = kadane_algorithm(a, len(a))

#PRINT INFO
print("Generated array:")
print(a)
print("")
print("Divide and Conquer algorithm:")
print("The maximum subarray sum:  ", max_sum_subarray_dac[2])
print("The start index of the subarray: ", max_sum_subarray_dac[0])
print("The end index of the subarray: ", max_sum_subarray_dac[1])
print("")
print("Kadane algorithm:")
print("The maximum subarray sum:  ", max_sum_subarray_kadane[0])
print("The start index of the subarray: ", max_sum_subarray_kadane[1])
print("The end index of the subarray: ", max_sum_subarray_kadane[2])
