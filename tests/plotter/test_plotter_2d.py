"""Tests for the Plotter2D class."""

import math
import os
import tempfile

import matplotlib

matplotlib.use("Agg")  # Use non-interactive backend for testing

import matplotlib.pyplot as plt

from calculuskit.plotter.plotter_2d import Plotter2D


def test_plotter_2d_basic_plot() -> None:
    """Test basic 2D plot creation."""

    def f(x: float) -> float:
        return x**2

    plotter = Plotter2D(f, x_range=(-5, 5))
    fig = plotter.plot(show=False)

    assert fig is not None
    plt.close(fig)


def test_plotter_2d_plot_with_styling() -> None:
    """Test 2D plot with custom styling."""

    def f(x: float) -> float:
        return math.sin(x)

    plotter = Plotter2D(f, x_range=(0, 2 * math.pi))
    fig = plotter.plot(
        title="Custom Sine",
        xlabel="x-axis",
        ylabel="y-axis",
        color="red",
        linestyle="--",
        linewidth=3.0,
        show=False,
    )

    assert fig is not None
    axes = fig.get_axes()[0]
    assert axes.get_title() == "Custom Sine"
    plt.close(fig)


def test_plotter_2d_plot_with_derivative() -> None:
    """Test plotting function with derivative."""

    def f(x: float) -> float:
        return x**2

    def df(x: float) -> float:
        return 2 * x

    plotter = Plotter2D(f, x_range=(-3, 3))
    fig = plotter.plot_with_derivative(df, show=False)

    assert fig is not None
    axes = fig.get_axes()[0]
    lines = axes.get_lines()
    assert len(lines) == 4  # 2 main plots + 2 axis lines
    plt.close(fig)


def test_plotter_2d_plot_multiple() -> None:
    """Test plotting multiple functions."""

    def sin_func(x: float) -> float:
        return math.sin(x)

    def cos_func(x: float) -> float:
        return math.cos(x)

    functions = [(sin_func, "sin(x)"), (cos_func, "cos(x)")]

    plotter = Plotter2D(sin_func, x_range=(0, 2 * math.pi))
    fig = plotter.plot_multiple(functions, show=False)

    assert fig is not None
    axes = fig.get_axes()[0]
    lines = axes.get_lines()
    assert len(lines) == 4  # 2 main plots + 2 axis lines
    plt.close(fig)


def test_plotter_2d_parametric_circle() -> None:
    """Test parametric plot of a circle."""

    def x_func(t: float) -> float:
        return math.cos(t)

    def y_func(t: float) -> float:
        return math.sin(t)

    plotter = Plotter2D(lambda x: x)
    fig = plotter.plot_parametric(
        x_func, y_func, t_range=(0, 2 * math.pi), title="Circle", show=False
    )

    assert fig is not None
    plt.close(fig)


def test_plotter_2d_polar_cardioid() -> None:
    """Test polar plot of a cardioid."""

    def r_func(angle: float) -> float:
        return 1 + math.cos(angle)

    plotter = Plotter2D(lambda x: x)
    fig = plotter.plot_polar(r_func, title="Cardioid", show=False)

    assert fig is not None
    plt.close(fig)


def test_plotter_2d_scatter_basic() -> None:
    """Test basic scatter plot."""
    x_data = [1.0, 2.0, 3.0, 4.0, 5.0]
    y_data = [2.1, 3.9, 6.2, 8.1, 9.8]

    plotter = Plotter2D(lambda x: x)
    fig = plotter.scatter_plot(x_data, y_data, show=False)

    assert fig is not None
    plt.close(fig)


def test_plotter_2d_scatter_with_fit() -> None:
    """Test scatter plot with polynomial fit."""
    x_data = [1.0, 2.0, 3.0, 4.0, 5.0]
    y_data = [1.1, 3.9, 9.2, 15.8, 25.1]

    plotter = Plotter2D(lambda x: x)
    fig = plotter.scatter_plot(x_data, y_data, show_fit=True, fit_degree=2, show=False)

    assert fig is not None
    axes = fig.get_axes()[0]
    lines = axes.get_lines()
    assert len(lines) == 1  # Fit line
    plt.close(fig)


def test_plotter_2d_save_plot() -> None:
    """Test saving plot to file."""

    def f(x: float) -> float:
        return x**2

    plotter = Plotter2D(f, x_range=(-5, 5))

    with tempfile.TemporaryDirectory() as tmpdir:
        save_path = os.path.join(tmpdir, "test_2d_plot.png")
        fig = plotter.plot(show=False, save_path=save_path)

        assert os.path.exists(save_path)
        assert os.path.getsize(save_path) > 0
        plt.close(fig)


def test_plotter_2d_multiple_with_colors() -> None:
    """Test multiple functions with custom colors."""

    def f1(x: float) -> float:
        return x

    def f2(x: float) -> float:
        return x**2

    functions = [(f1, "linear"), (f2, "quadratic")]
    colors = ["red", "blue"]

    plotter = Plotter2D(f1, x_range=(-2, 2))
    fig = plotter.plot_multiple(functions, colors=colors, show=False)

    assert fig is not None
    plt.close(fig)


def test_plotter_2d_parametric_spiral() -> None:
    """Test parametric plot of a spiral."""

    def x_func(t: float) -> float:
        return t * math.cos(t)

    def y_func(t: float) -> float:
        return t * math.sin(t)

    plotter = Plotter2D(lambda x: x)
    fig = plotter.plot_parametric(
        x_func, y_func, t_range=(0, 4 * math.pi), title="Spiral", show=False
    )

    assert fig is not None
    plt.close(fig)


def test_plotter_2d_inheritance() -> None:
    """Test that Plotter2D properly inherits from BasePlotter."""

    def f(x: float) -> float:
        return x**2

    plotter = Plotter2D(f, x_range=(0, 5))

    # Should have BasePlotter methods
    assert hasattr(plotter, "get_values")
    assert hasattr(plotter, "_compute_values")

    x_vals, y_vals = plotter.get_values()
    assert isinstance(x_vals, list)
    assert isinstance(y_vals, list)
