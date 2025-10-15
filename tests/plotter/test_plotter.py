"""Tests for the FunctionPlotter class."""

import math
import os
import tempfile

import matplotlib
import numpy as np

matplotlib.use("Agg")  # Use non-interactive backend for testing

from calculuskit.plotter import FunctionPlotter

# Initialization Tests


def test_init_default_parameters() -> None:
    """Test initialization with default parameters."""

    def f(x: float) -> float:
        return x**2

    plotter = FunctionPlotter(f)
    assert plotter.func == f
    assert plotter.x_range == (-10, 10)
    assert plotter.n_points == 1000


def test_init_custom_parameters() -> None:
    """Test initialization with custom parameters."""

    def f(x: float) -> float:
        return x**3

    plotter = FunctionPlotter(f, x_range=(-5, 5), n_points=500)
    assert plotter.func == f
    assert plotter.x_range == (-5, 5)
    assert plotter.n_points == 500


# Computation Tests


def test_compute_values() -> None:
    """Test computation of x and y values."""

    def f(x: float) -> float:
        return 2 * x

    plotter = FunctionPlotter(f, x_range=(0, 10), n_points=11)
    x_vals, y_vals = plotter._compute_values()

    assert len(x_vals) == 11
    assert len(y_vals) == 11
    assert x_vals[0] == 0
    assert x_vals[-1] == 10
    assert np.allclose(y_vals, 2 * x_vals)


def test_get_values() -> None:
    """Test get_values method returns lists."""

    def f(x: float) -> float:
        return x**2

    plotter = FunctionPlotter(f, x_range=(0, 5), n_points=6)
    x_vals, y_vals = plotter.get_values()

    assert isinstance(x_vals, list)
    assert isinstance(y_vals, list)
    assert len(x_vals) == 6
    assert len(y_vals) == 6


def test_compute_values_caching() -> None:
    """Test that computed values are cached."""

    def f(x: float) -> float:
        return x**2

    plotter = FunctionPlotter(f)
    x_vals1, y_vals1 = plotter._compute_values()
    x_vals2, y_vals2 = plotter._compute_values()

    # Should return the same cached objects
    assert x_vals1 is x_vals2
    assert y_vals1 is y_vals2


# Basic Plot Tests


def test_plot_basic() -> None:
    """Test basic plot creation."""

    def f(x: float) -> float:
        return x**2

    plotter = FunctionPlotter(f, x_range=(-5, 5))
    fig = plotter.plot(show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_plot_with_custom_styling() -> None:
    """Test plot with custom styling parameters."""

    def f(x: float) -> float:
        return math.sin(x)

    plotter = FunctionPlotter(f, x_range=(0, 2 * math.pi))
    fig = plotter.plot(
        title="Custom Title",
        xlabel="Custom X",
        ylabel="Custom Y",
        color="red",
        linestyle="--",
        linewidth=3.0,
        grid=False,
        figsize=(8, 6),
        show=False,
    )

    assert fig is not None
    axes = fig.get_axes()[0]
    assert axes.get_title() == "Custom Title"
    assert axes.get_xlabel() == "Custom X"
    assert axes.get_ylabel() == "Custom Y"
    matplotlib.pyplot.close(fig)


def test_plot_save_to_file() -> None:
    """Test saving plot to file."""

    def f(x: float) -> float:
        return x**2

    plotter = FunctionPlotter(f)

    with tempfile.TemporaryDirectory() as tmpdir:
        save_path = os.path.join(tmpdir, "test_plot.png")
        fig = plotter.plot(show=False, save_path=save_path)

        assert os.path.exists(save_path)
        assert os.path.getsize(save_path) > 0
        matplotlib.pyplot.close(fig)


# Derivative Plot Tests


def test_plot_with_derivative() -> None:
    """Test plotting function with its derivative."""

    def f(x: float) -> float:
        return x**2

    def df(x: float) -> float:
        return 2 * x

    plotter = FunctionPlotter(f, x_range=(-3, 3))
    fig = plotter.plot_with_derivative(df, show=False)

    assert fig is not None
    axes = fig.get_axes()[0]
    lines = axes.get_lines()
    # 2 main plots + 2 axis lines (at x=0 and y=0)
    assert len(lines) == 4
    matplotlib.pyplot.close(fig)


def test_plot_with_derivative_custom_labels() -> None:
    """Test derivative plot with custom labels."""

    def f(x: float) -> float:
        return x**3

    def df(x: float) -> float:
        return 3 * x**2

    plotter = FunctionPlotter(f)
    fig = plotter.plot_with_derivative(
        df,
        title="Cubic Function",
        func_label="f(x) = x³",
        deriv_label="f'(x) = 3x²",
        func_color="blue",
        deriv_color="green",
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


# Multiple Functions Tests


def test_plot_multiple_functions() -> None:
    """Test plotting multiple functions on same axes."""

    def sin_func(x: float) -> float:
        return math.sin(x)

    def cos_func(x: float) -> float:
        return math.cos(x)

    functions = [(sin_func, "sin(x)"), (cos_func, "cos(x)")]

    plotter = FunctionPlotter(sin_func, x_range=(0, 2 * math.pi))
    fig = plotter.plot_multiple(functions, show=False)

    assert fig is not None
    axes = fig.get_axes()[0]
    lines = axes.get_lines()
    # 2 main plots + 2 axis lines (at x=0 and y=0)
    assert len(lines) == 4
    matplotlib.pyplot.close(fig)


def test_plot_multiple_with_custom_colors() -> None:
    """Test multiple functions with custom colors."""

    def f1(x: float) -> float:
        return x

    def f2(x: float) -> float:
        return x**2

    def f3(x: float) -> float:
        return x**3

    functions = [(f1, "linear"), (f2, "quadratic"), (f3, "cubic")]
    colors = ["red", "green", "blue"]

    plotter = FunctionPlotter(f1, x_range=(-2, 2))
    fig = plotter.plot_multiple(functions, colors=colors, show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


# Parametric Tests


def test_plot_parametric_circle() -> None:
    """Test parametric plot of a circle."""

    def x_func(t: float) -> float:
        return math.cos(t)

    def y_func(t: float) -> float:
        return math.sin(t)

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.plot_parametric(x_func, y_func, t_range=(0, 2 * math.pi), show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_plot_parametric_custom_range() -> None:
    """Test parametric plot with custom parameter range."""

    def x_func(t: float) -> float:
        return t * math.cos(t)

    def y_func(t: float) -> float:
        return t * math.sin(t)

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.plot_parametric(
        x_func,
        y_func,
        t_range=(0, 4 * math.pi),
        title="Spiral",
        color="red",
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


# Polar Tests


def test_plot_polar_circle() -> None:
    """Test polar plot of a circle."""

    def r_func(_angle: float) -> float:
        return 1.0

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.plot_polar(r_func, show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_plot_polar_cardioid() -> None:
    """Test polar plot of a cardioid."""

    def r_func(angle: float) -> float:
        return 1 + math.cos(angle)

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.plot_polar(r_func, title="Cardioid", color="purple", show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_plot_polar_custom_range() -> None:
    """Test polar plot with custom theta range."""

    def r_func(angle: float) -> float:
        return angle

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.plot_polar(r_func, theta_range=(0, 4 * math.pi), title="Spiral", show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


# Scatter Plot Tests


def test_scatter_plot_basic() -> None:
    """Test basic scatter plot."""
    x_data = [1.0, 2.0, 3.0, 4.0, 5.0]
    y_data = [2.1, 3.9, 6.2, 8.1, 9.8]

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.scatter_plot(x_data, y_data, show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_scatter_plot_with_fit() -> None:
    """Test scatter plot with polynomial fit."""
    x_data = [1.0, 2.0, 3.0, 4.0, 5.0]
    y_data = [1.1, 3.9, 9.2, 15.8, 25.1]

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.scatter_plot(x_data, y_data, show_fit=True, fit_degree=2, show=False)

    assert fig is not None
    axes = fig.get_axes()[0]
    lines = axes.get_lines()
    assert len(lines) == 1  # Fit line
    matplotlib.pyplot.close(fig)


def test_scatter_plot_custom_styling() -> None:
    """Test scatter plot with custom styling."""
    x_data = [1.0, 2.0, 3.0, 4.0]
    y_data = [1.0, 4.0, 9.0, 16.0]

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.scatter_plot(
        x_data,
        y_data,
        color="red",
        marker="^",
        size=100,
        alpha=0.5,
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


# Edge Case Tests


def test_plot_constant_function() -> None:
    """Test plotting a constant function."""

    def f(_x: float) -> float:
        return 5.0

    plotter = FunctionPlotter(f, x_range=(0, 10))
    fig = plotter.plot(show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_plot_negative_range() -> None:
    """Test plotting with negative x range."""

    def f(x: float) -> float:
        return x**2

    plotter = FunctionPlotter(f, x_range=(-10, -1))
    fig = plotter.plot(show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_plot_exponential_function() -> None:
    """Test plotting exponential function."""

    def f(x: float) -> float:
        return math.exp(x)

    plotter = FunctionPlotter(f, x_range=(-2, 2))
    fig = plotter.plot(show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_plot_logarithmic_function() -> None:
    """Test plotting logarithmic function."""

    def f(x: float) -> float:
        return math.log(x)

    plotter = FunctionPlotter(f, x_range=(0.1, 10))
    fig = plotter.plot(show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_plot_with_zero_range() -> None:
    """Test behavior with very small range."""

    def f(x: float) -> float:
        return x**2

    plotter = FunctionPlotter(f, x_range=(5, 5.01), n_points=10)
    fig = plotter.plot(show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


# Trigonometric Tests


def test_plot_sine() -> None:
    """Test plotting sine function."""

    def f(x: float) -> float:
        return math.sin(x)

    plotter = FunctionPlotter(f, x_range=(0, 4 * math.pi))
    fig = plotter.plot(title="Sine Function", show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_plot_cosine() -> None:
    """Test plotting cosine function."""

    def f(x: float) -> float:
        return math.cos(x)

    plotter = FunctionPlotter(f, x_range=(0, 4 * math.pi))
    fig = plotter.plot(title="Cosine Function", show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_plot_tangent() -> None:
    """Test plotting tangent function."""

    def f(x: float) -> float:
        return math.tan(x)

    plotter = FunctionPlotter(f, x_range=(-1.5, 1.5))
    fig = plotter.plot(title="Tangent Function", show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


# Integration Tests


def test_plot_with_derivative_class() -> None:
    """Test plotting with Derivative class from CalculusKit."""
    from calculuskit.derivative.derivative import Derivative

    def f(val: float) -> float:
        return val**3

    derivative = Derivative(f)
    plotter = FunctionPlotter(f, x_range=(-2, 2))
    fig = plotter.plot_with_derivative(derivative, show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_plot_function_and_integral() -> None:
    """Test plotting a function that could be used with Integral class."""

    def f(x: float) -> float:
        return x**2

    # Antiderivative of x^2 is x^3/3
    def F(x: float) -> float:
        return x**3 / 3

    plotter = FunctionPlotter(f)
    functions = [(f, "f(x) = x²"), (F, "F(x) = x³/3")]
    fig = plotter.plot_multiple(functions, show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


# Contour Plot Tests


def test_contour_plot_basic() -> None:
    """Test basic contour plot creation."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.contour_plot(f, x_range=(-5, 5), y_range=(-5, 5), show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_contour_plot_saddle_point() -> None:
    """Test contour plot of a saddle point function."""

    def saddle(x: float, y: float) -> float:
        return x**2 - y**2

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.contour_plot(saddle, x_range=(-3, 3), y_range=(-3, 3), show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_contour_plot_with_custom_levels() -> None:
    """Test contour plot with custom number of levels."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.contour_plot(
        f,
        x_range=(-5, 5),
        y_range=(-5, 5),
        levels=30,
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_contour_plot_line_contours() -> None:
    """Test contour plot with line contours (not filled)."""

    def f(x: float, y: float) -> float:
        return math.sin(x) * math.cos(y)

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.contour_plot(
        f,
        x_range=(-math.pi, math.pi),
        y_range=(-math.pi, math.pi),
        filled=False,
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_contour_plot_custom_colormap() -> None:
    """Test contour plot with custom colormap."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.contour_plot(
        f,
        x_range=(-5, 5),
        y_range=(-5, 5),
        colormap="coolwarm",
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_contour_plot_without_colorbar() -> None:
    """Test contour plot without colorbar."""

    def f(x: float, y: float) -> float:
        return x * y

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.contour_plot(
        f,
        x_range=(-3, 3),
        y_range=(-3, 3),
        show_colorbar=False,
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_contour_plot_gaussian() -> None:
    """Test contour plot of a Gaussian function."""

    def gaussian(x: float, y: float) -> float:
        return math.exp(-(x**2 + y**2))

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.contour_plot(
        gaussian,
        x_range=(-3, 3),
        y_range=(-3, 3),
        title="2D Gaussian",
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_contour_plot_save_to_file() -> None:
    """Test saving contour plot to file."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = FunctionPlotter(lambda x: x)

    with tempfile.TemporaryDirectory() as tmpdir:
        save_path = os.path.join(tmpdir, "test_contour.png")
        fig = plotter.contour_plot(
            f,
            x_range=(-5, 5),
            y_range=(-5, 5),
            show=False,
            save_path=save_path,
        )

        assert os.path.exists(save_path)
        assert os.path.getsize(save_path) > 0
        matplotlib.pyplot.close(fig)


def test_contour_plot_asymmetric_ranges() -> None:
    """Test contour plot with different x and y ranges."""

    def f(x: float, y: float) -> float:
        return x**2 / 4 + y**2

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.contour_plot(
        f,
        x_range=(-10, 10),
        y_range=(-5, 5),
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_contour_plot_trigonometric() -> None:
    """Test contour plot of trigonometric function."""

    def f(x: float, y: float) -> float:
        return math.sin(x) * math.sin(y)

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.contour_plot(
        f,
        x_range=(0, 2 * math.pi),
        y_range=(0, 2 * math.pi),
        levels=25,
        colormap="RdBu",
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


# 3D Surface Plot Tests


def test_surface_plot_3d_basic() -> None:
    """Test basic 3D surface plot creation."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.surface_plot_3d(f, x_range=(-5, 5), y_range=(-5, 5), show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_surface_plot_3d_with_contour() -> None:
    """Test 3D surface plot with contour projection."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.surface_plot_3d(
        f,
        x_range=(-5, 5),
        y_range=(-5, 5),
        show_contour=True,
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_surface_plot_3d_saddle() -> None:
    """Test 3D surface plot of saddle point."""

    def saddle(x: float, y: float) -> float:
        return x**2 - y**2

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.surface_plot_3d(
        saddle,
        x_range=(-3, 3),
        y_range=(-3, 3),
        title="Saddle Point",
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_surface_plot_3d_custom_viewing_angle() -> None:
    """Test 3D surface plot with custom viewing angles."""

    def f(x: float, y: float) -> float:
        return math.sin(math.sqrt(x**2 + y**2))

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.surface_plot_3d(
        f,
        x_range=(-5, 5),
        y_range=(-5, 5),
        elevation=45,
        azimuth=60,
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_surface_plot_3d_custom_colormap() -> None:
    """Test 3D surface plot with custom colormap."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.surface_plot_3d(
        f,
        x_range=(-5, 5),
        y_range=(-5, 5),
        colormap="plasma",
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_surface_plot_3d_with_transparency() -> None:
    """Test 3D surface plot with custom transparency."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.surface_plot_3d(
        f,
        x_range=(-5, 5),
        y_range=(-5, 5),
        alpha=0.7,
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_surface_plot_3d_save_to_file() -> None:
    """Test saving 3D surface plot to file."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = FunctionPlotter(lambda x: x)

    with tempfile.TemporaryDirectory() as tmpdir:
        save_path = os.path.join(tmpdir, "test_3d_surface.png")
        fig = plotter.surface_plot_3d(
            f,
            x_range=(-5, 5),
            y_range=(-5, 5),
            show=False,
            save_path=save_path,
        )

        assert os.path.exists(save_path)
        assert os.path.getsize(save_path) > 0
        matplotlib.pyplot.close(fig)


# Quiver Plot (Vector Field) Tests


def test_quiver_plot_basic() -> None:
    """Test basic quiver plot creation."""

    def u(x: float, _y: float) -> float:
        return 2 * x

    def v(_x: float, y: float) -> float:
        return 2 * y

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.quiver_plot(u, v, x_range=(-5, 5), y_range=(-5, 5), show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_quiver_plot_rotation_field() -> None:
    """Test quiver plot of a rotation field."""

    def u(_x: float, y: float) -> float:
        return -y

    def v(x: float, _y: float) -> float:
        return x

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.quiver_plot(u, v, x_range=(-3, 3), y_range=(-3, 3), show=False)

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_quiver_plot_with_magnitude_coloring() -> None:
    """Test quiver plot with magnitude-based coloring."""

    def u(x: float, _y: float) -> float:
        return x

    def v(_x: float, y: float) -> float:
        return y

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.quiver_plot(
        u,
        v,
        x_range=(-5, 5),
        y_range=(-5, 5),
        show_magnitude=True,
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_quiver_plot_normalized() -> None:
    """Test quiver plot with normalized vectors."""

    def u(x: float, _y: float) -> float:
        return x

    def v(_x: float, y: float) -> float:
        return y

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.quiver_plot(
        u,
        v,
        x_range=(-5, 5),
        y_range=(-5, 5),
        normalize=True,
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_quiver_plot_custom_density() -> None:
    """Test quiver plot with custom arrow density."""

    def u(_x: float, y: float) -> float:
        return -y

    def v(x: float, _y: float) -> float:
        return x

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.quiver_plot(
        u,
        v,
        x_range=(-3, 3),
        y_range=(-3, 3),
        density=10,  # Fewer arrows
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_quiver_plot_custom_color() -> None:
    """Test quiver plot with custom color."""

    def u(x: float, _y: float) -> float:
        return x

    def v(_x: float, y: float) -> float:
        return y

    plotter = FunctionPlotter(lambda x: x)
    fig = plotter.quiver_plot(
        u,
        v,
        x_range=(-3, 3),
        y_range=(-3, 3),
        color="red",
        show=False,
    )

    assert fig is not None
    matplotlib.pyplot.close(fig)


def test_quiver_plot_save_to_file() -> None:
    """Test saving quiver plot to file."""

    def u(x: float, _y: float) -> float:
        return x

    def v(_x: float, y: float) -> float:
        return y

    plotter = FunctionPlotter(lambda x: x)

    with tempfile.TemporaryDirectory() as tmpdir:
        save_path = os.path.join(tmpdir, "test_quiver.png")
        fig = plotter.quiver_plot(
            u,
            v,
            x_range=(-5, 5),
            y_range=(-5, 5),
            show=False,
            save_path=save_path,
        )

        assert os.path.exists(save_path)
        assert os.path.getsize(save_path) > 0
        matplotlib.pyplot.close(fig)


# Animation Tests


def test_animate_series_approximation_basic() -> None:
    """Test basic series approximation animation."""

    def f(x: float) -> float:
        return math.exp(x)

    def taylor_approx(x: float, n: int) -> float:
        return sum(x**k / math.factorial(k) for k in range(n + 1))

    plotter = FunctionPlotter(f, x_range=(-2, 2))

    # Close any previous plots
    matplotlib.pyplot.close("all")

    # Animation methods don't have show parameter, they create animation objects
    # We just verify the animation can be created without errors
    try:
        anim = plotter.animate_series_approximation(
            f,
            taylor_approx,
            max_terms=5,
        )
        assert anim is not None
    finally:
        matplotlib.pyplot.close("all")


def test_animate_series_approximation_with_custom_title() -> None:
    """Test series approximation animation with custom title function."""

    def f(x: float) -> float:
        return math.sin(x)

    def taylor_approx(x: float, n: int) -> float:
        result = 0.0
        for k in range(n + 1):
            sign = (-1) ** k
            result += sign * (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
        return result

    plotter = FunctionPlotter(f, x_range=(-math.pi, math.pi))

    matplotlib.pyplot.close("all")
    try:
        anim = plotter.animate_series_approximation(
            f,
            taylor_approx,
            max_terms=5,
            title_func=lambda n: f"Taylor Series Approximation: {n} terms",
        )
        assert anim is not None
    finally:
        matplotlib.pyplot.close("all")


def test_animate_limit_convergence_basic() -> None:
    """Test basic limit convergence animation."""

    def seq(n: int) -> float:
        return 1 / n

    plotter = FunctionPlotter(lambda x: x)

    matplotlib.pyplot.close("all")
    try:
        anim = plotter.animate_limit_convergence(
            seq,
            limit_value=0.0,
            max_n=20,
        )
        assert anim is not None
    finally:
        matplotlib.pyplot.close("all")


def test_animate_limit_convergence_to_e() -> None:
    """Test convergence animation to Euler's number."""

    def seq(n: int) -> float:
        return (1 + 1 / n) ** n

    plotter = FunctionPlotter(lambda x: x)

    matplotlib.pyplot.close("all")
    try:
        anim = plotter.animate_limit_convergence(
            seq,
            limit_value=math.e,
            max_n=30,
            title="Convergence to e",
        )
        assert anim is not None
    finally:
        matplotlib.pyplot.close("all")


def test_animate_limit_convergence_without_limit() -> None:
    """Test convergence animation without showing limit line."""

    def seq(n: int) -> float:
        return math.log(n) / n

    plotter = FunctionPlotter(lambda x: x)

    matplotlib.pyplot.close("all")
    try:
        anim = plotter.animate_limit_convergence(
            seq,
            limit_value=None,
            max_n=25,
        )
        assert anim is not None
    finally:
        matplotlib.pyplot.close("all")


def test_animate_limit_convergence_custom_styling() -> None:
    """Test convergence animation with custom styling."""

    def seq(n: int) -> float:
        return math.sin(n) / n

    plotter = FunctionPlotter(lambda x: x)

    matplotlib.pyplot.close("all")
    try:
        anim = plotter.animate_limit_convergence(
            seq,
            limit_value=0.0,
            max_n=30,
            sequence_color="blue",
            limit_color="red",
            marker="^",
        )
        assert anim is not None
    finally:
        matplotlib.pyplot.close("all")
