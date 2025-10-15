"""Basic integral examples using CalculusKit."""

import math

from calculuskit.integral.integral import Integral


def example_1_simple_polynomial():
    """Example 1: Integral of x^2."""
    print("=" * 60)
    print("Example 1: Integral of f(x) = x^2 from 0 to 1")
    print("=" * 60)

    def f(x):
        return x**2

    # Create an integral object
    integral = Integral(f)

    # Calculate definite integral from 0 to 1
    # Expected: ∫x^2 dx from 0 to 1 = [x^3/3] = 1/3 ≈ 0.3333
    result = integral.between(0, 1)
    print(f"∫₀¹ x² dx = {result}")
    print(f"Expected: {1 / 3:.6f}")
    print()


def example_2_different_methods():
    """Example 2: Comparing different integration methods."""
    print("=" * 60)
    print("Example 2: Different integration methods for f(x) = sin(x)")
    print("=" * 60)

    def f(x):
        return math.sin(x)

    a, b = 0, math.pi

    # Trapezoidal rule
    int_trap = Integral(f, method="trapezoidal", n=1000)
    result_trap = int_trap.between(a, b)
    print(f"Trapezoidal rule: {result_trap}")

    # Simpson's rule (most accurate for smooth functions)
    int_simpson = Integral(f, method="simpson", n=1000)
    result_simpson = int_simpson.between(a, b)
    print(f"Simpson's rule: {result_simpson}")

    # Midpoint rule
    int_mid = Integral(f, method="midpoint", n=1000)
    result_mid = int_mid.between(a, b)
    print(f"Midpoint rule: {result_mid}")

    # Expected: ∫sin(x)dx from 0 to π = [-cos(x)] = -cos(π) + cos(0) = 2
    print("Expected: 2.0")
    print()


def example_3_exponential():
    """Example 3: Integral of exponential function."""
    print("=" * 60)
    print("Example 3: Integral of f(x) = e^x from 0 to 1")
    print("=" * 60)

    def f(x):
        return math.exp(x)

    integral = Integral(f, n=1000)

    # ∫e^x dx from 0 to 1 = [e^x] = e - 1
    result = integral.definite(0, 1)
    expected = math.e - 1

    print(f"∫₀¹ e^x dx = {result}")
    print(f"Expected (e - 1): {expected}")
    print(f"Error: {abs(result - expected)}")
    print()


def example_4_cumulative_integral():
    """Example 4: Cumulative integral."""
    print("=" * 60)
    print("Example 4: Cumulative integral of f(x) = x")
    print("=" * 60)

    def f(x):
        return x

    integral = Integral(f)

    # Get cumulative integral from 0 to 4
    x_vals, cumulative_vals = integral.cumulative(0, 4, num_points=5)

    print("Cumulative integral values:")
    print("x | ∫₀ˣ t dt | Expected (x²/2)")
    print("-" * 40)
    for x, cum_val in zip(x_vals, cumulative_vals):
        expected = x**2 / 2
        print(f"{x:4.1f} | {cum_val:8.4f} | {expected:8.4f}")
    print()


def example_5_average_value():
    """Example 5: Average value of a function."""
    print("=" * 60)
    print("Example 5: Average value of f(x) = sin(x) from 0 to π")
    print("=" * 60)

    def f(x):
        return math.sin(x)

    integral = Integral(f, n=1000)

    # Average value = (1/(b-a)) * ∫ₐᵇ f(x) dx
    avg = integral.average_value(0, math.pi)

    print(f"Average value: {avg}")
    # Expected: (1/π) * 2 = 2/π ≈ 0.6366
    print(f"Expected (2/π): {2 / math.pi}")
    print()


def example_6_area_under_curve():
    """Example 6: Finding area under a curve."""
    print("=" * 60)
    print("Example 6: Area under f(x) = x² + 1 from -2 to 2")
    print("=" * 60)

    def f(x):
        return x**2 + 1

    integral = Integral(f, method="simpson", n=1000)

    area = integral.between(-2, 2)

    # Expected: ∫(x² + 1)dx from -2 to 2 = [x³/3 + x] = (8/3 + 2) - (-8/3 - 2) = 16/3 + 4 = 28/3
    expected = 28 / 3

    print(f"Area: {area}")
    print(f"Expected: {expected:.6f}")
    print(f"Error: {abs(area - expected):.6f}")
    print()


if __name__ == "__main__":
    example_1_simple_polynomial()
    example_2_different_methods()
    example_3_exponential()
    example_4_cumulative_integral()
    example_5_average_value()
    example_6_area_under_curve()

    print("=" * 60)
    print("All integral examples completed!")
    print("=" * 60)
