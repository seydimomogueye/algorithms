def subarrays_with_product_less_than_target(A, target):
    """
    Given a array with positive numbers and a target number, find all it contiguous subarrays whose
    product is less than the target number.
    """
    result = []
    tmp_A = []
    left_pointer = 0
    partial_product = A[0]

    if A[left_pointer] < target:
        tmp_A.append(A[left_pointer])
        result.append([A[left_pointer]])

    for right_pointer in range(1, len(A)):
        if A[right_pointer] < target:
            result.append([A[right_pointer]])
            tmp_A.append(A[right_pointer])

        partial_product = partial_product * A[right_pointer]
        
        if partial_product < target:
            result.append(tmp_A[:])
        else:
            while left_pointer < right_pointer-1:
                del tmp_A[0]
                partial_product = partial_product / A[left_pointer]
                left_pointer += 1

                if partial_product < target:
                    result.append(tmp_A[:])

    return result



# print(subarrays_with_product_less_than_target(
#         A=[1, 2, 5, 3, 10], target=30))

print(subarrays_with_product_less_than_target(
        A=[8, 2, 6, 5], target=50))

