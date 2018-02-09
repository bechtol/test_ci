import numpy as np

def test_addition():
    """
    Addition test
    """
    a, b = 2, 2
    x = a + b
    np.testing.assert_almost_equal(x, 4.)

def test_subtraction():
    """
    Subtraction test
    """
    a, b = 10, 7
    x = a - b
    np.testing.assert_almost_equal(x, 3.)

def test_multiplication():
    """
    Multiplication test
    """
    a, b = 3, 8
    x = a * b
    np.testing.assert_almost_equal(x, 24.)

if __name__ == '__main__':
    np.testing.run_module_suite()
