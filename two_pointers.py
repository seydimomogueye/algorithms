import math

from collections import deque


def subarrays_with_product_less_than_target(A, target):
    """
    Given a Aay with positive numbers and a target number, find all it contiguous subAays whose
    product is less than the target number.
    Learned:
    """

    result = []
    product = 1
    left = 0
    for right in range(len(A)):
        product *= A[right]
        while (product >= target and left < len(A)):
            product /= A[left]
            left += 1
        
        temp_list = deque()
        for i in range(right, left-1, -1):
            temp_list.appendleft(A[i])
            result.append(list(temp_list))

    return result


def dutch_flag_sort(A):
    """
    Problem:
    --
    Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.
    The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

    Tips:
    --
    """
    low, high = 0, len(A) - 1
    i = 0
    while(i <= high):
        if A[i] == 0:
            A[i], A[low] = A[low], A[i]
            i += 1
            low += 1
        elif A[i] == 1:
            i += 1
        else:
            A[i], A[high] = A[high], A[i]
            high -= 1

    return A


def quadruple_sum_to_target(A, target):
    """
    Problem:
    --
    Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

    Tips:
    --
    """
    quadruplets = []

    for i in range(len(A) - 1):
        left_pointer = i + 1
        right_pointer = len(A) - 1

        x = target - (A[i] + A[left_pointer] + A[right_pointer])
        cursor = left_pointer + 1

        while cursor < right_pointer:
            if x == A[cursor]:
                quadruplets.append([A[i], A[left_pointer], A[cursor], A[right_pointer]])
            cursor += 1

    return quadruplets


def get_next_valid_index(s, index):
    backspace_count = 0

    while index >= 0:
        if s[index] == "#":
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break
        
        index -= 1
    
    return index


def comparing_strings_containing_backspace(string_1, string_2):
    """
    Problem:
    --
    Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

    Tips:
    --
    """

    ptr_s1 = len(string_1) - 1
    ptr_s2 = len(string_2) - 1

    while (ptr_s1 >= 0 and ptr_s2 >= 0):
        i1 = get_next_valid_index(string_1, ptr_s1)
        i2 = get_next_valid_index(string_2, ptr_s2)

        if string_1[i1] != string_2[i2]:
            return False
        
        if i1 < 0 or i2 < 0:
            return False
        
        if i1 < 0 and i2 < 0:
            return True
        
        ptr_s1 = i1 - 1
        ptr_s2 = i2 - 1

    return True


def minimum_window_sort(A):
    """
    Problem:
    Learned:
    """

    low = 0
    high = len(A) - 1

    while low < len(A) - 1 and A[low] <= A[low+1]:
        low += 1
    
    if low == len(A) - 1:
        return 0
    
    while high > 0 and A[high] >= A[high - 1]:
        high -= 1
    
    subarray_max = -math.inf
    subarray_min = math.inf

    for k in range(low, high+1):
        subarray_max = max(subarray_max, A[k])
        subarray_min = min(subarray_min, A[k])
    
    while low > 0 and A[low-1] > subarray_min:
        low -= 1
    
    while high < len(A) - 1 and A[high + 1] < subarray_max:
        high += 1
    
    return high - low + 1
