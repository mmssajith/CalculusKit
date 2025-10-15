"""Test cases for Limit class."""

import math

from calculuskit.limit.limit import Limit


def test_limit_polynomial():
    """Test limit of polynomial function."""

    def f(x):
        return (x**2 - 1) / (x - 1)

    lim = Limit(f)

    # Limit as x approaches 1 should be 2
    result = lim.at(1.0)
    assert abs(result - 2.0) < 1e-5


def test_limit_rational():
    """Test limit of rational function."""

    def f(x):
        return (x**2 - 4) / (x - 2)

    lim = Limit(f)

    # Limit as x approaches 2 should be 4
    result = lim.at(2.0)
    assert abs(result - 4.0) < 1e-5


def test_limit_trig():
    """Test limit of sin(x)/x as x approaches 0."""

    def f(x):
        if x == 0:
            return 1
        return math.sin(x) / x

    lim = Limit(f)

    # Limit as x approaches 0 should be 1
    result = lim.at(0.0)
    assert abs(result - 1.0) < 1e-5


def test_limit_left():
    """Test left-hand limit."""

    def f(x):
        return x**2

    lim = Limit(f)

    result = lim.left(2.0)
    assert abs(result - 4.0) < 1e-5


def test_limit_right():
    """Test right-hand limit."""

    def f(x):
        return x**2

    lim = Limit(f)

    result = lim.right(2.0)
    assert abs(result - 4.0) < 1e-5


def test_limit_exists():
    """Test if limit exists."""

    def f(x):
        return x**2

    lim = Limit(f)

    assert lim.exists(2.0) is True


def test_limit_does_not_exist():
    """Test when limit does not exist."""

    def f(x):
        if x < 1:
            return 0
        else:
            return 1

    lim = Limit(f)

    # Limit at x=1 should not exist (discontinuous)
    assert lim.exists(1.0) is False


def test_is_continuous():
    """Test continuity check."""

    def f(x):
        return x**2

    lim = Limit(f)

    assert lim.is_continuous(2.0) is True


def test_is_not_continuous():
    """Test discontinuity check."""

    def f(x):
        if x == 1:
            return 5
        return (x**2 - 1) / (x - 1)

    lim = Limit(f)

    # Function has a removable discontinuity at x=1
    assert lim.is_continuous(1.0) is False


def test_limit_as_x_approaches_infinity():
    """Test limit as x approaches infinity."""

    def f(x):
        return 1 / x

    lim = Limit(f)

    result = lim.as_x_approaches_infinity(direction="positive")
    assert result is not None
    assert abs(result) < 1e-5


def test_limit_exp_growth():
    """Test limit of exponential function."""

    def f(x):
        return math.exp(x)

    lim = Limit(f)

    # Limit as x approaches 0 should be 1
    result = lim.at(0.0)
    assert abs(result - 1.0) < 1e-5
