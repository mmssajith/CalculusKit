"""Test cases for Derivative class."""

import math

from calculuskit.derivative.derivative import Derivative


def test_derivative_quadratic():
    """Test derivative of quadratic function x^2."""

    def f(x):
        return x**2

    df = Derivative(f)

    # Derivative of x^2 at x=3 should be 2*3 = 6
    assert abs(df.at(3.0) - 6.0) < 1e-5


def test_derivative_cubic():
    """Test derivative of cubic function x^3."""

    def f(x):
        return x**3

    df = Derivative(f)

    # Derivative of x^3 at x=2 should be 3*2^2 = 12
    assert abs(df.at(2.0) - 12.0) < 1e-4


def test_derivative_sin():
    """Test derivative of sin(x)."""
    df = Derivative(math.sin)

    # Derivative of sin(x) at x=0 should be cos(0) = 1
    assert abs(df.at(0.0) - 1.0) < 1e-5

    # Derivative of sin(x) at x=pi/2 should be cos(pi/2) = 0
    assert abs(df.at(math.pi / 2)) < 1e-5


def test_derivative_exp():
    """Test derivative of e^x."""
    df = Derivative(math.exp)

    # Derivative of e^x at x=1 should be e^1
    assert abs(df.at(1.0) - math.exp(1.0)) < 1e-4


def test_derivative_callable():
    """Test that derivative object is callable."""

    def f(x):
        return x**2

    df = Derivative(f)

    # Test __call__ method
    assert abs(df(3.0) - 6.0) < 1e-5


def test_derivative_forward_method():
    """Test forward difference method."""

    def f(x):
        return x**2

    df = Derivative(f, method="forward")
    assert abs(df.at(3.0) - 6.0) < 1e-5


def test_derivative_backward_method():
    """Test backward difference method."""

    def f(x):
        return x**2

    df = Derivative(f, method="backward")
    assert abs(df.at(3.0) - 6.0) < 1e-5


def test_derivative_central_method():
    """Test central difference method."""

    def f(x):
        return x**2

    df = Derivative(f, method="central")
    assert abs(df.at(3.0) - 6.0) < 1e-5


def test_gradient_method():
    """Test gradient method returns correct shape."""

    def f(x):
        return x**2

    df = Derivative(f)
    x_vals, deriv_vals = df.gradient(3.0, dx=1.0, n_points=50)

    assert len(x_vals) == 50
    assert len(deriv_vals) == 50
