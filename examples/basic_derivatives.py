"""Basic derivative examples using CalculusKit."""

import math

from calculuskit.derivative.derivative import Derivative


def example_1_simple_polynomial():
    """Example 1: Derivative of x^2."""
    print("=" * 60)
    print("Example 1: Derivative of f(x) = x^2")
    print("=" * 60)

    def f(x):
        return x**2

    # Create a derivative object
    df = Derivative(f)

    # Calculate derivative at x = 3
    # Expected: f'(3) = 2*3 = 6
    result = df.at(3.0)
    print(f"f'(3) = {result}")
    print("Expected: 6.0")
    print()


def example_2_different_methods():
    """Example 2: Comparing different differentiation methods."""
    print("=" * 60)
    print("Example 2: Different differentiation methods for f(x) = sin(x)")
    print("=" * 60)

    def f(x):
        return math.sin(x)

    x = math.pi / 4  # 45 degrees

    # Forward difference
    df_forward = Derivative(f, method="forward")
    print(f"Forward difference at π/4: {df_forward.at(x)}")

    # Backward difference
    df_backward = Derivative(f, method="backward")
    print(f"Backward difference at π/4: {df_backward.at(x)}")

    # Central difference (most accurate)
    df_central = Derivative(f, method="central")
    print(f"Central difference at π/4: {df_central.at(x)}")

    # Expected value: cos(π/4) ≈ 0.7071
    print(f"Expected (cos(π/4)): {math.cos(x)}")
    print()


def example_3_exponential():
    """Example 3: Derivative of exponential function."""
    print("=" * 60)
    print("Example 3: Derivative of f(x) = e^x")
    print("=" * 60)

    def f(x):
        return math.exp(x)

    df = Derivative(f)

    # For e^x, the derivative is also e^x
    x = 2.0
    result = df.at(x)
    expected = math.exp(x)

    print(f"f'({x}) = {result}")
    print(f"Expected (e^{x}): {expected}")
    print(f"Error: {abs(result - expected)}")
    print()


def example_4_gradient():
    """Example 4: Calculate gradient over a range."""
    print("=" * 60)
    print("Example 4: Gradient of f(x) = x^3 - 3x + 2")
    print("=" * 60)

    def f(x):
        return x**3 - 3 * x + 2

    df = Derivative(f)

    # Get gradient around x = 1
    x_vals, deriv_vals = df.gradient(x=1.0, dx=2.0, n_points=5)

    print("x values and their derivatives:")
    for x, dy in zip(x_vals, deriv_vals):
        print(f"  x = {x:6.2f}, f'(x) = {dy:8.4f}")
    print()


def example_5_callable():
    """Example 5: Using derivative object as a function."""
    print("=" * 60)
    print("Example 5: Derivative object as callable")
    print("=" * 60)

    def f(x):
        return x**2 + 2 * x + 1  # (x+1)^2

    df = Derivative(f)

    # Can call df directly
    print("f(x) = x^2 + 2x + 1 = (x+1)^2")
    print("f'(x) = 2x + 2 = 2(x+1)")
    print()

    for x in [-2, -1, 0, 1, 2]:
        result = df(x)  # Using __call__
        expected = 2 * x + 2
        print(f"x = {x:2d}: f'(x) = {result:6.2f}, expected = {expected:6.2f}")
    print()


if __name__ == "__main__":
    example_1_simple_polynomial()
    example_2_different_methods()
    example_3_exponential()
    example_4_gradient()
    example_5_callable()

    print("=" * 60)
    print("All derivative examples completed!")
    print("=" * 60)
