from . import two_pointers


def test_subarrays_with_product_less_than_target():
    results_1 = two_pointers.subarrays_with_product_less_than_target(
            [2, 5, 3, 10], 30)
    
    results_2 = two_pointers.subarrays_with_product_less_than_target(
            [8, 2, 6, 5], 50)
    
    assert results_1 == [[2], [5], [2, 5], [3], [5, 3], [10]]
    
    assert results_2 == [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]


def test_dutch_flag_sort():
    result_1 = two_pointers.dutch_flag_sort([1, 0, 2, 1, 0])
    result_2 = two_pointers.dutch_flag_sort([2, 2, 0, 1, 2, 0])

    assert result_1 == [0, 0, 1, 1, 2]
    assert result_2 == [0, 0, 1, 2, 2, 2]


def test_quadruplet_sum_to_target():
    result_1 = two_pointers.quadruple_sum_to_target(
            [4, 1, 2, -1, 1, -3], 1)
    result_2 = two_pointers.quadruple_sum_to_target(
            [2, 0, -1, 1, -2, 2], 2)

    assert [sum(a) for a in result_1] == [sum([-3, -1, 1, 4]), sum([-3, 1, 1, 2])]
    assert [sum(a) for a in result_2] == [sum([-2, 0, 2, 2]), sum([-1, 0, 1, 2])]


def test_comparing_strings_containing_backspace():
    result_1 = two_pointers.comparing_strings_containing_backspace(
            "xy#z", "xzz#")
    result_2 = two_pointers.comparing_strings_containing_backspace(
            "xy#z", "xyz#")
    result_3 = two_pointers.comparing_strings_containing_backspace(
            "xp#", "xyz##")
    result_4 = two_pointers.comparing_strings_containing_backspace(
            "xywrrmp", "xywrrmu#p")
    
    assert result_1 == True
    assert result_2 == False
    assert result_3 == True
    assert result_4 == True


def test_minimum_window_sort():
    result_1 = two_pointers.minimum_window_sort(
            [1, 2, 5, 3, 7, 10, 9, 12])
    result_2 = two_pointers.minimum_window_sort(
            [1, 3, 2, 0, -1, 7, 10])
    result_3 = two_pointers.minimum_window_sort(
            [1, 2, 3])
    result_4 = two_pointers.minimum_window_sort(
            [3, 2, 1])
    
    assert result_1 == 5
    assert result_2 == 5
    assert result_3 == 0
    assert result_4 == 3