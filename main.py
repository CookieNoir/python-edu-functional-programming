import pytest


def launch_tests():
    pytest.main(["tests/func_only_tests.py"])


if __name__ == '__main__':
    launch_tests()
