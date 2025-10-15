"""Test cases for FourierSeries class."""

import math

import numpy as np

from calculuskit.fourier_series.fourier_series import FourierSeries


def test_fourier_series_constant():
    """Test Fourier series of constant function."""

    fourier = FourierSeries(lambda _x: 1.0, period=2 * math.pi, n=5)

    # a0 coefficient should be 1
    a0 = fourier.a0()
    assert abs(a0 - 1.0) < 0.1


def test_fourier_series_sin():
    """Test Fourier series of sine function."""

    def f(x):
        return math.sin(x)

    fourier = FourierSeries(f, period=2 * math.pi, n=10)

    # Fourier series should approximate sin(x)
    result = fourier.at(math.pi / 4)
    expected = math.sin(math.pi / 4)
    assert abs(result - expected) < 0.2


def test_fourier_series_cos():
    """Test Fourier series of cosine function."""

    def f(x):
        return math.cos(x)

    fourier = FourierSeries(f, period=2 * math.pi, n=10)

    # Fourier series should approximate cos(x)
    result = fourier.at(math.pi / 4)
    expected = math.cos(math.pi / 4)
    assert abs(result - expected) < 0.2


def test_fourier_series_square_wave():
    """Test Fourier series of square wave."""

    def square_wave(x):
        normalized_x = x % (2 * math.pi)
        return 1.0 if normalized_x < math.pi else -1.0

    fourier = FourierSeries(square_wave, period=2 * math.pi, n=20)

    # Test at a point where square wave is 1
    result = fourier.at(math.pi / 2)
    assert result > 0.5


def test_fourier_a0_coefficient():
    """Test a0 coefficient calculation."""

    fourier = FourierSeries(lambda _x: 2.0, period=2 * math.pi, n=5)

    a0 = fourier.a0()
    assert abs(a0 - 2.0) < 0.1


def test_fourier_an_coefficient():
    """Test an (cosine) coefficient calculation."""

    def f(x):
        return math.cos(2 * x)

    fourier = FourierSeries(f, period=2 * math.pi, n=5)

    # For cos(2x), a2 should be non-zero
    a2 = fourier.an(2)
    assert abs(a2) > 0.1


def test_fourier_bn_coefficient():
    """Test bn (sine) coefficient calculation."""

    def f(x):
        return math.sin(x)

    fourier = FourierSeries(f, period=2 * math.pi, n=5)

    # For sin(x), b1 should be non-zero
    b1 = fourier.bn(1)
    assert abs(b1) > 0.1


def test_fourier_series_evaluation():
    """Test Fourier series evaluation at multiple points."""

    def f(x):
        return x

    fourier = FourierSeries(f, period=2 * math.pi, n=10)

    # Evaluate at a point
    result = fourier.at(1.0)
    assert isinstance(result, (float, np.floating))


def test_fourier_series_different_period():
    """Test Fourier series with different period."""

    fourier = FourierSeries(lambda _x: 1.0, period=4 * math.pi, n=5)

    a0 = fourier.a0()
    assert abs(a0 - 1.0) < 0.1


def test_fourier_series_symmetry():
    """Test Fourier series for even and odd functions."""

    # Even function (cos)
    def even_f(x):
        return math.cos(x)

    fourier_even = FourierSeries(even_f, period=2 * math.pi, n=5)

    # Odd function (sin)
    def odd_f(x):
        return math.sin(x)

    fourier_odd = FourierSeries(odd_f, period=2 * math.pi, n=5)

    # Both should work without errors
    result_even = fourier_even.at(1.0)
    result_odd = fourier_odd.at(1.0)

    assert isinstance(result_even, (float, np.floating))
    assert isinstance(result_odd, (float, np.floating))
