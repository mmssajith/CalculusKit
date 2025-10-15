"""Test cases for Integral class."""

import math

from calculuskit.integral.integral import Integral


def test_integral_quadratic():
    """Test integral of x^2 from 0 to 1."""

    def f(x):
        return x**2

    integral = Integral(f)

    # Integral of x^2 from 0 to 1 should be 1/3
    result = integral.between(0, 1)
    assert abs(result - 1 / 3) < 1e-3


def test_integral_cubic():
    """Test integral of x^3 from 0 to 2."""

    def f(x):
        return x**3

    integral = Integral(f)

    # Integral of x^3 from 0 to 2 should be 4
    result = integral.between(0, 2)
    assert abs(result - 4.0) < 1e-2


def test_integral_sin():
    """Test integral of sin(x)."""
    integral = Integral(math.sin)

    # Integral of sin(x) from 0 to pi should be 2
    result = integral.between(0, math.pi)
    assert abs(result - 2.0) < 1e-3


def test_integral_exp():
    """Test integral of e^x."""
    integral = Integral(math.exp)

    # Integral of e^x from 0 to 1 should be e - 1
    result = integral.between(0, 1)
    expected = math.exp(1) - 1
    assert abs(result - expected) < 1e-3


def test_integral_definite_alias():
    """Test definite method as alias for between."""

    def f(x):
        return x**2

    integral = Integral(f)

    result1 = integral.between(0, 1)
    result2 = integral.definite(0, 1)

    assert abs(result1 - result2) < 1e-10


def test_integral_trapezoidal_method():
    """Test trapezoidal integration method."""

    def f(x):
        return x**2

    integral = Integral(f, method="trapezoidal")
    result = integral.between(0, 1)

    assert abs(result - 1 / 3) < 1e-3


def test_integral_simpson_method():
    """Test Simpson's rule integration method."""

    def f(x):
        return x**2

    integral = Integral(f, method="simpson")
    result = integral.between(0, 1)

    assert abs(result - 1 / 3) < 1e-4


def test_integral_midpoint_method():
    """Test midpoint integration method."""

    def f(x):
        return x**2

    integral = Integral(f, method="midpoint")
    result = integral.between(0, 1)

    assert abs(result - 1 / 3) < 1e-3


def test_cumulative_integral():
    """Test cumulative integral calculation."""

    def f(x):
        return x

    integral = Integral(f)
    x_vals, cumulative_vals = integral.cumulative(0, 2, num_points=10)

    assert len(x_vals) == 10
    assert len(cumulative_vals) == 10

    # Integral of x from 0 to 2 should be 2
    assert abs(cumulative_vals[-1] - 2.0) < 1e-2


def test_average_value():
    """Test average value calculation."""

    def f(x):
        return x**2

    integral = Integral(f)

    # Average value of x^2 from 0 to 1 should be 1/3
    avg = integral.average_value(0, 1)
    assert abs(avg - 1 / 3) < 1e-3
