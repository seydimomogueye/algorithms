def cyclic_sort(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i +=1
    return nums


# print(cyclic_sort([3, 1, 5, 4, 2]))


def find_the_missing_number(A):
    size, i = len(A), 0

    while i < size:
        j = A[i]
        if A[i] < size and A[j] != A[i]:
            A[j], A[i] = A[i], A[j]
        else:
            i += 1
    
    for i in range(size):
        if A[i] == i:
            continue
        return i

    return -1


print(find_the_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))

