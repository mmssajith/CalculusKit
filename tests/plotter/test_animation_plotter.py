"""Tests for the AnimationPlotter class."""

import math

import matplotlib

matplotlib.use("Agg")  # Use non-interactive backend for testing

import matplotlib.pyplot as plt

from calculuskit.plotter.animation_plotter import AnimationPlotter


def test_animation_plotter_series_approximation_basic() -> None:
    """Test basic series approximation animation."""

    def f(x: float) -> float:
        return math.exp(x)

    def taylor_approx(x: float, n: int) -> float:
        return sum(x**k / math.factorial(k) for k in range(n + 1))

    plotter = AnimationPlotter(f, x_range=(-2, 2))

    plt.close("all")
    try:
        anim = plotter.animate_series_approximation(
            f,
            taylor_approx,
            max_terms=5,
        )
        assert anim is not None
    finally:
        plt.close("all")


def test_animation_plotter_series_approximation_custom_title() -> None:
    """Test series approximation animation with custom title."""

    def f(x: float) -> float:
        return math.sin(x)

    def taylor_approx(x: float, n: int) -> float:
        result = 0.0
        for k in range(n + 1):
            sign = (-1) ** k
            result += sign * (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
        return result

    plotter = AnimationPlotter(f, x_range=(-math.pi, math.pi))

    plt.close("all")
    try:
        anim = plotter.animate_series_approximation(
            f,
            taylor_approx,
            max_terms=5,
            title_func=lambda n: f"Taylor Series: {n} terms",
        )
        assert anim is not None
    finally:
        plt.close("all")


def test_animation_plotter_limit_convergence_basic() -> None:
    """Test basic limit convergence animation."""

    def seq(n: int) -> float:
        return 1 / n

    plotter = AnimationPlotter(lambda x: x)

    plt.close("all")
    try:
        anim = plotter.animate_limit_convergence(
            seq,
            limit_value=0.0,
            max_n=20,
        )
        assert anim is not None
    finally:
        plt.close("all")


def test_animation_plotter_limit_convergence_to_e() -> None:
    """Test convergence animation to Euler's number."""

    def seq(n: int) -> float:
        return (1 + 1 / n) ** n

    plotter = AnimationPlotter(lambda x: x)

    plt.close("all")
    try:
        anim = plotter.animate_limit_convergence(
            seq,
            limit_value=math.e,
            max_n=30,
            title="Convergence to e",
        )
        assert anim is not None
    finally:
        plt.close("all")


def test_animation_plotter_limit_convergence_without_limit() -> None:
    """Test convergence animation without showing limit line."""

    def seq(n: int) -> float:
        return math.log(n) / n

    plotter = AnimationPlotter(lambda x: x)

    plt.close("all")
    try:
        anim = plotter.animate_limit_convergence(
            seq,
            limit_value=None,
            max_n=25,
        )
        assert anim is not None
    finally:
        plt.close("all")


def test_animation_plotter_limit_convergence_custom_styling() -> None:
    """Test convergence animation with custom styling."""

    def seq(n: int) -> float:
        return math.sin(n) / n

    plotter = AnimationPlotter(lambda x: x)

    plt.close("all")
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
        plt.close("all")


def test_animation_plotter_series_with_custom_colors() -> None:
    """Test series approximation with custom colors."""

    def f(x: float) -> float:
        return math.cos(x)

    def taylor_approx(x: float, n: int) -> float:
        result = 0.0
        for k in range(n + 1):
            sign = (-1) ** k
            result += sign * (x ** (2 * k)) / math.factorial(2 * k)
        return result

    plotter = AnimationPlotter(f, x_range=(-math.pi, math.pi))

    plt.close("all")
    try:
        anim = plotter.animate_series_approximation(
            f,
            taylor_approx,
            max_terms=5,
            func_color="green",
            approx_color="orange",
        )
        assert anim is not None
    finally:
        plt.close("all")


def test_animation_plotter_inheritance() -> None:
    """Test that AnimationPlotter properly inherits from BasePlotter."""

    def f(x: float) -> float:
        return x**2

    plotter = AnimationPlotter(f, x_range=(0, 5))

    # Should have BasePlotter methods
    assert hasattr(plotter, "get_values")
    assert hasattr(plotter, "_compute_values")

    x_vals, y_vals = plotter.get_values()
    assert isinstance(x_vals, list)
    assert isinstance(y_vals, list)


def test_animation_plotter_series_custom_range() -> None:
    """Test series approximation with custom range."""

    def f(x: float) -> float:
        return math.exp(x)

    def taylor_approx(x: float, n: int) -> float:
        return sum(x**k / math.factorial(k) for k in range(n + 1))

    plotter = AnimationPlotter(f, x_range=(-1, 1))

    plt.close("all")
    try:
        anim = plotter.animate_series_approximation(
            f,
            taylor_approx,
            x_range=(-1, 1),
            max_terms=8,
        )
        assert anim is not None
    finally:
        plt.close("all")


def test_animation_plotter_limit_convergence_custom_interval() -> None:
    """Test limit convergence with custom interval."""

    def seq(n: int) -> float:
        return 1 / (n**2)

    plotter = AnimationPlotter(lambda x: x)

    plt.close("all")
    try:
        anim = plotter.animate_limit_convergence(
            seq,
            limit_value=0.0,
            max_n=20,
            interval=100,  # Faster animation
        )
        assert anim is not None
    finally:
        plt.close("all")
