from . import two_pointers


def test_subarrays_with_product_less_than_target():
    results_1 = two_pointers.subarrays_with_product_less_than_target(
            A=[2, 5, 3, 10], target=30)
    
    results_2 = two_pointers.subarrays_with_product_less_than_target(
            A=[8, 2, 6, 5], target=50)
    
    assert results_1 == [[2], [5], [2, 5], [3], [5, 3], [10]]
    
    assert results_2 == [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]

