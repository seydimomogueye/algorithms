"""
Mastering Cyclic sort Algorithms.
--
1. Make sure that the max element it's less or equal Array size.
2. We can only have one duplicate eleme,t per item.
"""

def cyclic_sort(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i +=1
    return nums



def find_the_missing_number(A):
    A_size, i = len(A), 0

    while i < A_size:
        j = A[i]
        if A[j] != A[i]:
            A[j], A[i] = A[j], A[i]
        else:
            i += 1
    
    for i in range(A_size):
        if A[i] == i:
            continue
        return i

    return -1



def find_all_missing_numbers(A):
    missing_numbers = []
    size = len(A)
    i = 0

    while(i < size):
        j = A[i] - 1

        if j < len(A) and A[i] != A[j]:
            A[i], A[j] = A[j], A[i]
        else:
            i += 1

    for i in range(1, size):
        if i == A[i]:
            continue
        missing_numbers.append(i)

    return missing_numbers


def find_duplicate(A):
    pass



def find_all_duplicate_numbers(A):
    pass