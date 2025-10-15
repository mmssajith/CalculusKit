"""Tests for the Plotter3D class."""

import math
import os
import tempfile

import matplotlib

matplotlib.use("Agg")  # Use non-interactive backend for testing

import matplotlib.pyplot as plt

from calculuskit.plotter.plotter_3d import Plotter3D


def test_plotter_3d_contour_basic() -> None:
    """Test basic contour plot."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = Plotter3D(lambda x: x)
    fig = plotter.contour_plot(f, x_range=(-5, 5), y_range=(-5, 5), show=False)

    assert fig is not None
    plt.close(fig)


def test_plotter_3d_contour_saddle() -> None:
    """Test contour plot of saddle point."""

    def saddle(x: float, y: float) -> float:
        return x**2 - y**2

    plotter = Plotter3D(lambda x: x)
    fig = plotter.contour_plot(saddle, x_range=(-3, 3), y_range=(-3, 3), show=False)

    assert fig is not None
    plt.close(fig)


def test_plotter_3d_contour_custom_levels() -> None:
    """Test contour plot with custom levels."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = Plotter3D(lambda x: x)
    fig = plotter.contour_plot(
        f,
        x_range=(-5, 5),
        y_range=(-5, 5),
        levels=30,
        show=False,
    )

    assert fig is not None
    plt.close(fig)


def test_plotter_3d_contour_line_contours() -> None:
    """Test contour plot with line contours."""

    def f(x: float, y: float) -> float:
        return math.sin(x) * math.cos(y)

    plotter = Plotter3D(lambda x: x)
    fig = plotter.contour_plot(
        f,
        x_range=(-math.pi, math.pi),
        y_range=(-math.pi, math.pi),
        filled=False,
        show=False,
    )

    assert fig is not None
    plt.close(fig)


def test_plotter_3d_contour_custom_colormap() -> None:
    """Test contour plot with custom colormap."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = Plotter3D(lambda x: x)
    fig = plotter.contour_plot(
        f,
        x_range=(-5, 5),
        y_range=(-5, 5),
        colormap="coolwarm",
        show=False,
    )

    assert fig is not None
    plt.close(fig)


def test_plotter_3d_contour_without_colorbar() -> None:
    """Test contour plot without colorbar."""

    def f(x: float, y: float) -> float:
        return x * y

    plotter = Plotter3D(lambda x: x)
    fig = plotter.contour_plot(
        f,
        x_range=(-3, 3),
        y_range=(-3, 3),
        show_colorbar=False,
        show=False,
    )

    assert fig is not None
    plt.close(fig)


def test_plotter_3d_surface_basic() -> None:
    """Test basic 3D surface plot."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = Plotter3D(lambda x: x)
    fig = plotter.surface_plot_3d(f, x_range=(-5, 5), y_range=(-5, 5), show=False)

    assert fig is not None
    plt.close(fig)


def test_plotter_3d_surface_with_contour() -> None:
    """Test 3D surface plot with contour projection."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = Plotter3D(lambda x: x)
    fig = plotter.surface_plot_3d(
        f,
        x_range=(-5, 5),
        y_range=(-5, 5),
        show_contour=True,
        show=False,
    )

    assert fig is not None
    plt.close(fig)


def test_plotter_3d_surface_saddle() -> None:
    """Test 3D surface plot of saddle point."""

    def saddle(x: float, y: float) -> float:
        return x**2 - y**2

    plotter = Plotter3D(lambda x: x)
    fig = plotter.surface_plot_3d(
        saddle,
        x_range=(-3, 3),
        y_range=(-3, 3),
        title="Saddle Point",
        show=False,
    )

    assert fig is not None
    plt.close(fig)


def test_plotter_3d_surface_custom_viewing_angle() -> None:
    """Test 3D surface plot with custom viewing angle."""

    def f(x: float, y: float) -> float:
        return math.sin(math.sqrt(x**2 + y**2))

    plotter = Plotter3D(lambda x: x)
    fig = plotter.surface_plot_3d(
        f,
        x_range=(-5, 5),
        y_range=(-5, 5),
        elevation=45,
        azimuth=60,
        show=False,
    )

    assert fig is not None
    plt.close(fig)


def test_plotter_3d_surface_custom_colormap() -> None:
    """Test 3D surface plot with custom colormap."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = Plotter3D(lambda x: x)
    fig = plotter.surface_plot_3d(
        f,
        x_range=(-5, 5),
        y_range=(-5, 5),
        colormap="plasma",
        show=False,
    )

    assert fig is not None
    plt.close(fig)


def test_plotter_3d_surface_with_transparency() -> None:
    """Test 3D surface plot with transparency."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = Plotter3D(lambda x: x)
    fig = plotter.surface_plot_3d(
        f,
        x_range=(-5, 5),
        y_range=(-5, 5),
        alpha=0.7,
        show=False,
    )

    assert fig is not None
    plt.close(fig)


def test_plotter_3d_save_contour() -> None:
    """Test saving contour plot to file."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = Plotter3D(lambda x: x)

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
        plt.close(fig)


def test_plotter_3d_save_surface() -> None:
    """Test saving 3D surface plot to file."""

    def f(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = Plotter3D(lambda x: x)

    with tempfile.TemporaryDirectory() as tmpdir:
        save_path = os.path.join(tmpdir, "test_surface.png")
        fig = plotter.surface_plot_3d(
            f,
            x_range=(-5, 5),
            y_range=(-5, 5),
            show=False,
            save_path=save_path,
        )

        assert os.path.exists(save_path)
        assert os.path.getsize(save_path) > 0
        plt.close(fig)


def test_plotter_3d_inheritance() -> None:
    """Test that Plotter3D properly inherits from BasePlotter."""

    def f(x: float) -> float:
        return x**2

    plotter = Plotter3D(f, x_range=(0, 5))

    # Should have BasePlotter methods
    assert hasattr(plotter, "get_values")
    assert hasattr(plotter, "_compute_values")

    x_vals, y_vals = plotter.get_values()
    assert isinstance(x_vals, list)
    assert isinstance(y_vals, list)
