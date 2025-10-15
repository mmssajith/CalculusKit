"""Tests for the BasePlotter class."""

import math

import matplotlib

matplotlib.use("Agg")  # Use non-interactive backend for testing

import numpy as np

from calculuskit.plotter.base_plotter import BasePlotter


def test_base_plotter_init_default() -> None:
    """Test BasePlotter initialization with default parameters."""

    def f(x: float) -> float:
        return x**2

    plotter = BasePlotter(f)
    assert plotter.func == f
    assert plotter.x_range == (-10, 10)
    assert plotter.n_points == 1000
    assert plotter._x_values is None
    assert plotter._y_values is None


def test_base_plotter_init_custom() -> None:
    """Test BasePlotter initialization with custom parameters."""

    def f(x: float) -> float:
        return x**3

    plotter = BasePlotter(f, x_range=(-5, 5), n_points=500)
    assert plotter.func == f
    assert plotter.x_range == (-5, 5)
    assert plotter.n_points == 500


def test_base_plotter_compute_values() -> None:
    """Test computation of x and y values."""

    def f(x: float) -> float:
        return 2 * x + 1

    plotter = BasePlotter(f, x_range=(0, 10), n_points=11)
    x_vals, y_vals = plotter._compute_values()

    assert len(x_vals) == 11
    assert len(y_vals) == 11
    assert x_vals[0] == 0
    assert x_vals[-1] == 10
    assert np.allclose(y_vals, 2 * x_vals + 1)


def test_base_plotter_compute_values_caching() -> None:
    """Test that computed values are cached."""

    def f(x: float) -> float:
        return x**2

    plotter = BasePlotter(f)
    x_vals1, y_vals1 = plotter._compute_values()
    x_vals2, y_vals2 = plotter._compute_values()

    # Should return the same cached objects
    assert x_vals1 is x_vals2
    assert y_vals1 is y_vals2


def test_base_plotter_get_values() -> None:
    """Test get_values method returns lists."""

    def f(x: float) -> float:
        return x**2

    plotter = BasePlotter(f, x_range=(0, 5), n_points=6)
    x_vals, y_vals = plotter.get_values()

    assert isinstance(x_vals, list)
    assert isinstance(y_vals, list)
    assert len(x_vals) == 6
    assert len(y_vals) == 6


def test_base_plotter_vectorization() -> None:
    """Test that functions are properly vectorized."""

    def f(x: float) -> float:
        return math.sin(x)

    plotter = BasePlotter(f, x_range=(0, 2 * math.pi), n_points=100)
    x_vals, y_vals = plotter._compute_values()

    # Verify vectorization worked by checking values
    assert len(x_vals) == 100
    assert len(y_vals) == 100
    # Check first and last values
    assert np.isclose(y_vals[0], math.sin(x_vals[0]))
    assert np.isclose(y_vals[-1], math.sin(x_vals[-1]))


def test_base_plotter_negative_range() -> None:
    """Test BasePlotter with negative x range."""

    def f(x: float) -> float:
        return x**3

    plotter = BasePlotter(f, x_range=(-5, -1), n_points=5)
    x_vals, y_vals = plotter._compute_values()

    assert len(x_vals) == 5
    assert x_vals[0] == -5
    assert x_vals[-1] == -1
    assert all(y < 0 for y in y_vals)  # x^3 is negative for negative x


def test_base_plotter_single_point_range() -> None:
    """Test BasePlotter with a very small range."""

    def f(x: float) -> float:
        return x**2

    plotter = BasePlotter(f, x_range=(5, 5.1), n_points=10)
    x_vals, y_vals = plotter._compute_values()

    assert len(x_vals) == 10
    assert x_vals[0] == 5
    assert x_vals[-1] == 5.1
