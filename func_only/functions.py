from typing import Callable
from typing import Iterable


def is_empty(iterable: Iterable):
    match any(True for _ in iterable):
        case True:
            return False
        case _:
            return True


def non_empty(iterable: Iterable):
    return not is_empty(iterable)


def head(iterable: Iterable):
    match iterable:
        case h, *t:
            return h
        case _:
            return None


def tail(iterable: Iterable):
    match iterable:
        case h, *t:
            match any(True for _ in t):
                case True:
                    return t
                case _:
                    return None
        case _:
            return None


def print_all(iterable: Iterable):
    match iterable:
        case h, *t:
            print(h)
            print_all(t)


def generator_map(function: Callable, iterable: Iterable):
    def inner_generator(in_func, in_iterable):
        for item in in_iterable:
            yield in_func(item)

    return list(inner_generator(function, iterable))


def generator_filter(function: Callable, iterable: Iterable):
    def inner_generator(in_func, in_iterable):
        for item in in_iterable:
            match in_func(item):
                case True:
                    yield item

    return list(inner_generator(function, iterable))


def list_comp_map(function: Callable, iterable: Iterable):
    return [function(item) for item in iterable]


def list_comp_filter(function: Callable, iterable: Iterable):
    return [item for item in iterable if function(item)]


def matching_map(function: Callable, iterable: Iterable):
    match iterable:
        case item, *t:
            return [function(item)] + matching_map(function, t)
        case _:
            return []


def matching_filter(function: Callable, iterable: Iterable):
    def inner_filter(in_func, in_item):
        match in_func(in_item):
            case True:
                return [in_item]
            case _:
                return []

    match iterable:
        case item, *t:
            return inner_filter(function, item) + matching_filter(function, t)
        case _:
            return []


def reduce(function: Callable, iterable: Iterable, initializer=None):
    def inner_reduce(in_func, left, right: Iterable):
        match right:
            case h, *t:
                return in_func(left, inner_reduce(in_func, h, t))
            case _:
                return left

    match initializer:
        case None:
            match iterable:
                case h, *t:
                    return inner_reduce(function, h, t)
                case _:
                    raise TypeError
        case _:
            return inner_reduce(function, initializer, iterable)


# https://www.geeksforgeeks.org/quick-sort/
def quicksort(list_obj: list):
    match len(list_obj):
        case 0 | 1:
            return list_obj
        case _:
            return (quicksort([item for item in list_obj[:-1] if item <= list_obj[-1]])
                    + [list_obj[-1]]
                    + quicksort([item for item in list_obj[:-1] if item > list_obj[-1]]))
