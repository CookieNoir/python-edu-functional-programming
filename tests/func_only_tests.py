import pytest
from func_only import functions


def test_is_empty_no_elem_returns_true():
    obj = []
    assert functions.is_empty(obj) is True


def test_is_empty_one_elem_returns_false():
    obj = [3]
    assert functions.is_empty(obj) is False


def test_non_empty_one_elem_returns_true1():
    obj = [3]
    assert functions.non_empty(obj) is True


def test_non_empty_two_elem_returns_true2():
    obj = [3, 4]
    assert functions.non_empty(obj) is True


def test_non_empty_no_elem_returns_false():
    obj = []
    assert functions.non_empty(obj) is False


def test_head_one_elem_returns_2():
    obj = [2]
    assert functions.head(obj) == 2


def test_head_two_elem_returns_2():
    obj = [2, 3]
    assert functions.head(obj) == 2


def test_head_three_elem_returns_2():
    obj = [2, 3, 4]
    assert functions.head(obj) == 2


def test_head_no_elem_returns_none():
    obj = []
    assert functions.head(obj) is None


def test_tail_no_elem_returns_none():
    obj = []
    assert functions.tail(obj) is None


def test_tail_one_elem_returns_none():
    obj = [2]
    assert functions.tail(obj) is None


def test_tail_two_elem_returns_3():
    obj = [2, 3]
    assert functions.tail(obj) == [3]


def test_tail_three_elem_returns_34():
    obj = [2, 3, 4]
    assert functions.tail(obj) == [3, 4]


def test_print_all_no_elem_returns_nothing(capsys):
    obj = []
    functions.print_all(obj)
    captured = capsys.readouterr()
    assert captured.out == ""


def test_print_all_one_elem_returns_1(capsys):
    obj = [1]
    functions.print_all(obj)
    captured = capsys.readouterr()
    assert captured.out == "1\n"


def test_print_all_two_elem_returns_13(capsys):
    obj = [1, 3]
    functions.print_all(obj)
    captured = capsys.readouterr()
    assert captured.out == "1\n3\n"


def test_generator_map_no_elem_returns_empty_list():
    obj = []
    func = lambda x: x + 1
    assert functions.generator_map(func, obj) == []


def test_generator_map_filled_list_returns_2452():
    obj = [1, 3, 4, 1]
    func = lambda x: x + 1
    assert functions.generator_map(func, obj) == [2, 4, 5, 2]


def test_generator_filter_no_elem_returns_empty_list():
    obj = []
    func = lambda x: x > 3
    assert functions.generator_filter(func, obj) == []


def test_generator_filter_filled_list_returns_4648():
    obj = [2, 4, 3, 1, 6, 4, 8, 3]
    func = lambda x: x > 3
    assert functions.generator_filter(func, obj) == [4, 6, 4, 8]


def test_list_comp_map_no_elem_returns_empty_list():
    obj = []
    func = lambda x: x + 1
    assert functions.list_comp_map(func, obj) == []


def test_list_comp_map_filled_list_returns_2452():
    obj = [1, 3, 4, 1]
    func = lambda x: x + 1
    assert functions.list_comp_map(func, obj) == [2, 4, 5, 2]


def test_list_comp_filter_no_elem_returns_empty_list():
    obj = []
    func = lambda x: x > 3
    assert functions.list_comp_filter(func, obj) == []


def test_list_comp_filter_filled_list_returns_4648():
    obj = [2, 4, 3, 1, 6, 4, 8, 3]
    func = lambda x: x > 3
    assert functions.list_comp_filter(func, obj) == [4, 6, 4, 8]


def test_matching_map_no_elem_returns_empty_list():
    obj = []
    func = lambda x: x + 1
    assert functions.matching_map(func, obj) == []


def test_matching_map_1_elem_returns_2():
    obj = [1]
    func = lambda x: x + 1
    assert functions.matching_map(func, obj) == [2]


def test_matching_map_filled_list_returns_2452():
    obj = [1, 3, 4, 1]
    func = lambda x: x + 1
    assert functions.matching_map(func, obj) == [2, 4, 5, 2]


def test_matching_filter_no_elem_returns_empty_list():
    obj = []
    func = lambda x: x > 3
    assert functions.matching_filter(func, obj) == []


def test_matching_filter_1_elem_returns_empty_list():
    obj = [2]
    func = lambda x: x > 3
    assert functions.matching_filter(func, obj) == []


def test_matching_filter_filled_list_returns_4648():
    obj = [2, 4, 3, 1, 6, 4, 8, 3]
    func = lambda x: x > 3
    print(functions.matching_filter(func, obj))
    assert functions.matching_filter(func, obj) == [4, 6, 4, 8]


def test_reduce_no_elem_tuple_returns_TypeError():
    obj = ()
    func = lambda a, b: max(a, b)
    with pytest.raises(TypeError):
        functions.reduce(func, obj)


def test_reduce_1_elem_tuple_returns_3():
    obj = (3,)
    func = lambda a, b: max(a, b)
    assert functions.reduce(func, obj) == 3


def test_reduce_with_initializer_1_elem_tuple_returns_5():
    obj = (3,)
    func = lambda a, b: max(a, b)
    assert functions.reduce(func, obj, 5) == 5


def test_reduce_with_initializer_2_elem_tuple_returns_7():
    obj = (3, 7)
    func = lambda a, b: max(a, b)
    assert functions.reduce(func, obj, 5) == 7


def test_reduce_3_elem_tuple_returns_7():
    obj = (3, 7, 1)
    func = lambda a, b: max(a, b)
    assert functions.reduce(func, obj) == 7


def test_reduce_3_elem_list_returns_7():
    obj = [3, 7, 1]
    func = lambda a, b: max(a, b)
    assert functions.reduce(func, obj) == 7


def test_quicksort_no_elem_returns_empty_list():
    obj = []
    assert functions.quicksort(obj) == []


def test_quicksort_1_elem_returns_2():
    obj = [2]
    assert functions.quicksort(obj) == [2]


def test_quicksort_filled_list_returns_123456():
    obj = [4, 3, 1, 6, 5, 2]
    assert functions.quicksort(obj) == [1, 2, 3, 4, 5, 6]
