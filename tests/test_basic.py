import numpy as np

def test_basic():
    """
    Most basic test
    """
    a, b = 2, 2
    x = a + b
    np.testing.assert_almost_equal(x, 4.)

if __name__ == '__main__':
    np.testing.run_module_suite()
