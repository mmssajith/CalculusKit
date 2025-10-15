"""Tests for the VectorFieldPlotter class."""

import os
import tempfile

import matplotlib

matplotlib.use("Agg")  # Use non-interactive backend for testing

import matplotlib.pyplot as plt

from calculuskit.plotter.vector_field_plotter import VectorFieldPlotter


def test_vector_field_plotter_basic() -> None:
    """Test basic quiver plot."""

    def u(x: float, _y: float) -> float:
        return 2 * x

    def v(_x: float, y: float) -> float:
        return 2 * y

    plotter = VectorFieldPlotter(lambda x: x)
    fig = plotter.quiver_plot(u, v, x_range=(-5, 5), y_range=(-5, 5), show=False)

    assert fig is not None
    plt.close(fig)


def test_vector_field_plotter_rotation() -> None:
    """Test quiver plot of rotation field."""

    def u(_x: float, y: float) -> float:
        return -y

    def v(x: float, _y: float) -> float:
        return x

    plotter = VectorFieldPlotter(lambda x: x)
    fig = plotter.quiver_plot(u, v, x_range=(-3, 3), y_range=(-3, 3), show=False)

    assert fig is not None
    plt.close(fig)


def test_vector_field_plotter_with_magnitude_coloring() -> None:
    """Test quiver plot with magnitude-based coloring."""

    def u(x: float, _y: float) -> float:
        return x

    def v(_x: float, y: float) -> float:
        return y

    plotter = VectorFieldPlotter(lambda x: x)
    fig = plotter.quiver_plot(
        u,
        v,
        x_range=(-5, 5),
        y_range=(-5, 5),
        show_magnitude=True,
        show=False,
    )

    assert fig is not None
    plt.close(fig)


def test_vector_field_plotter_normalized() -> None:
    """Test quiver plot with normalized vectors."""

    def u(x: float, _y: float) -> float:
        return x

    def v(_x: float, y: float) -> float:
        return y

    plotter = VectorFieldPlotter(lambda x: x)
    fig = plotter.quiver_plot(
        u,
        v,
        x_range=(-5, 5),
        y_range=(-5, 5),
        normalize=True,
        show=False,
    )

    assert fig is not None
    plt.close(fig)


def test_vector_field_plotter_custom_density() -> None:
    """Test quiver plot with custom arrow density."""

    def u(_x: float, y: float) -> float:
        return -y

    def v(x: float, _y: float) -> float:
        return x

    plotter = VectorFieldPlotter(lambda x: x)
    fig = plotter.quiver_plot(
        u,
        v,
        x_range=(-3, 3),
        y_range=(-3, 3),
        density=10,
        show=False,
    )

    assert fig is not None
    plt.close(fig)


def test_vector_field_plotter_custom_color() -> None:
    """Test quiver plot with custom color."""

    def u(x: float, _y: float) -> float:
        return x

    def v(_x: float, y: float) -> float:
        return y

    plotter = VectorFieldPlotter(lambda x: x)
    fig = plotter.quiver_plot(
        u,
        v,
        x_range=(-3, 3),
        y_range=(-3, 3),
        color="red",
        show=False,
    )

    assert fig is not None
    plt.close(fig)


def test_vector_field_plotter_custom_colormap() -> None:
    """Test quiver plot with custom colormap."""

    def u(x: float, _y: float) -> float:
        return x

    def v(_x: float, y: float) -> float:
        return y

    plotter = VectorFieldPlotter(lambda x: x)
    fig = plotter.quiver_plot(
        u,
        v,
        x_range=(-5, 5),
        y_range=(-5, 5),
        show_magnitude=True,
        colormap="plasma",
        show=False,
    )

    assert fig is not None
    plt.close(fig)


def test_vector_field_plotter_save() -> None:
    """Test saving quiver plot to file."""

    def u(x: float, _y: float) -> float:
        return x

    def v(_x: float, y: float) -> float:
        return y

    plotter = VectorFieldPlotter(lambda x: x)

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
        plt.close(fig)


def test_vector_field_plotter_gradient_field() -> None:
    """Test gradient field visualization."""

    # Gradient of f(x,y) = x^2 + y^2 is (2x, 2y)
    def u(x: float, _y: float) -> float:
        return 2 * x

    def v(_x: float, y: float) -> float:
        return 2 * y

    plotter = VectorFieldPlotter(lambda x: x)
    fig = plotter.quiver_plot(
        u,
        v,
        x_range=(-3, 3),
        y_range=(-3, 3),
        title="Gradient Field",
        show=False,
    )

    assert fig is not None
    plt.close(fig)


def test_vector_field_plotter_inheritance() -> None:
    """Test that VectorFieldPlotter properly inherits from BasePlotter."""

    def f(x: float) -> float:
        return x**2

    plotter = VectorFieldPlotter(f, x_range=(0, 5))

    # Should have BasePlotter methods
    assert hasattr(plotter, "get_values")
    assert hasattr(plotter, "_compute_values")

    x_vals, y_vals = plotter.get_values()
    assert isinstance(x_vals, list)
    assert isinstance(y_vals, list)


def test_vector_field_plotter_with_width_and_scale() -> None:
    """Test quiver plot with custom width and scale."""

    def u(_x: float, y: float) -> float:
        return -y

    def v(x: float, _y: float) -> float:
        return x

    plotter = VectorFieldPlotter(lambda x: x)
    fig = plotter.quiver_plot(
        u,
        v,
        x_range=(-3, 3),
        y_range=(-3, 3),
        width=0.005,
        scale=10,
        show=False,
    )

    assert fig is not None
    plt.close(fig)
