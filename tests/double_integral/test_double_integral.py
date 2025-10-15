"""Test cases for DoubleIntegral class."""

import math

from calculuskit.double_integral.double_integral import DoubleIntegral


def test_double_integral_product():
    """Test double integral of x * y."""

    def f(x, y):
        return x * y

    dbl_integral = DoubleIntegral(f)

    # Integral of x*y over [0,1] x [0,1] should be 1/4
    result = dbl_integral.over(0, 1, 0, 1)
    assert abs(result - 0.25) < 1e-2


def test_double_integral_sum():
    """Test double integral of x + y."""

    def f(x, y):
        return x + y

    dbl_integral = DoubleIntegral(f)

    # Integral of (x+y) over [0,1] x [0,1] should be 1
    result = dbl_integral.over(0, 1, 0, 1)
    assert abs(result - 1.0) < 1e-2


def test_double_integral_squares():
    """Test double integral of x^2 + y^2."""

    def f(x, y):
        return x**2 + y**2

    dbl_integral = DoubleIntegral(f)

    # Integral of (x^2 + y^2) over [0,1] x [0,1] should be 2/3
    result = dbl_integral.over(0, 1, 0, 1)
    assert abs(result - 2 / 3) < 1e-2


def test_double_integral_constant():
    """Test double integral of constant function."""

    dbl_integral = DoubleIntegral(lambda _x, _y: 1.0)

    # Integral of 1 over [0,2] x [0,3] should be 6
    result = dbl_integral.over(0, 2, 0, 3)
    assert abs(result - 6.0) < 1e-2


def test_double_integral_trig():
    """Test double integral with trigonometric functions."""

    def f(x, y):
        return math.sin(x) * math.cos(y)

    dbl_integral = DoubleIntegral(f, n=200)

    # Integral of sin(x)*cos(y) over [0,pi] x [0,pi/2]
    # should be 2 (since integral of sin(x) from 0 to pi is 2,
    # and integral of cos(y) from 0 to pi/2 is 1)
    result = dbl_integral.over(0, math.pi, 0, math.pi / 2)
    assert abs(result - 2.0) < 1e-1


def test_double_integral_rectangular_region():
    """Test double integral over different rectangular regions."""

    def f(x, y):
        return x * y

    dbl_integral = DoubleIntegral(f)

    # Integral of x*y over [0,2] x [0,2] should be 4
    result = dbl_integral.over(0, 2, 0, 2)
    assert abs(result - 4.0) < 1e-2


def test_double_integral_simpson_method():
    """Test double integral with Simpson's method."""

    def f(x, y):
        return x**2 + y**2

    dbl_integral = DoubleIntegral(f, method="simpson")
    result = dbl_integral.over(0, 1, 0, 1)

    assert abs(result - 2 / 3) < 1e-2
