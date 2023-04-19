from stepik_auto_tests_course.func_devision import division
import pytest

@pytest.mark.parametrize("a, b, expected_result",[(10,2,5), 
                                                  (10, 5, 2),
                                                  (20, -2, -10)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result