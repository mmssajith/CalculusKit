"""Basic limit examples using CalculusKit."""

import math

from calculuskit.limit.limit import Limit


def example_1_simple_limit():
    """Example 1: Simple limit."""
    print("=" * 60)
    print("Example 1: lim(x→2) of (x² - 4)/(x - 2)")
    print("=" * 60)

    def f(x):
        return (x**2 - 4) / (x - 2)

    # Create a limit object
    lim = Limit(f)

    # Calculate limit as x approaches 2
    # Note: f(2) is undefined, but lim = (x+2)(x-2)/(x-2) = x+2, so lim(x→2) = 4
    result = lim.at(2.0)
    print(f"lim(x→2) f(x) = {result}")
    print("Expected: 4.0")
    print()


def example_2_one_sided_limits():
    """Example 2: One-sided limits."""
    print("=" * 60)
    print("Example 2: One-sided limits of f(x) = 1/(x-1)")
    print("=" * 60)

    def f(x):
        return 1 / (x - 1)

    lim = Limit(f)

    x0 = 1.0

    # Left-hand limit (approaches from left, should be -∞)
    left_lim = lim.left(x0)
    print(f"lim(x→1⁻) f(x) = {left_lim}")

    # Right-hand limit (approaches from right, should be +∞)
    right_lim = lim.right(x0)
    print(f"lim(x→1⁺) f(x) = {right_lim}")

    # Check if limit exists (should be False since left ≠ right)
    exists = lim.exists(x0)
    print(f"Does limit exist at x=1? {exists}")
    print()


def example_3_continuity():
    """Example 3: Testing continuity."""
    print("=" * 60)
    print("Example 3: Testing continuity of f(x) = x² at x = 2")
    print("=" * 60)

    def f(x):
        return x**2

    lim = Limit(f)

    x0 = 2.0

    # Check if continuous (should be True for polynomials)
    is_cont = lim.is_continuous(x0)
    print(f"Is f(x) continuous at x={x0}? {is_cont}")

    # Compare with discontinuous function
    print()
    print("Now testing discontinuous function:")

    def g(x):
        if x != 2:
            return (x**2 - 4) / (x - 2)
        else:
            return 0  # Discontinuity at x=2

    lim_g = Limit(g)
    is_cont_g = lim_g.is_continuous(2.0)
    print(f"Is g(x) continuous at x=2? {is_cont_g}")
    print()


def example_4_trigonometric_limit():
    """Example 4: Trigonometric limit."""
    print("=" * 60)
    print("Example 4: lim(x→0) of sin(x)/x")
    print("=" * 60)

    def f(x):
        return math.sin(x) / x if x != 0 else 1

    lim = Limit(f)

    # This famous limit equals 1
    result = lim.at(0.0)
    print(f"lim(x→0) sin(x)/x = {result}")
    print("Expected: 1.0")
    print()


def example_5_limit_at_infinity():
    """Example 5: Limit at infinity."""
    print("=" * 60)
    print("Example 5: Limits at infinity")
    print("=" * 60)

    # Example: lim(x→∞) 1/x = 0
    def f(x):
        return 1 / x

    lim = Limit(f)

    result_pos = lim.as_x_approaches_infinity(direction="positive")
    print(f"lim(x→+∞) 1/x = {result_pos}")
    print("Expected: 0.0")

    result_neg = lim.as_x_approaches_infinity(direction="negative")
    print(f"lim(x→-∞) 1/x = {result_neg}")
    print("Expected: 0.0")
    print()


def example_6_exponential_limit():
    """Example 6: Exponential limit."""
    print("=" * 60)
    print("Example 6: lim(x→0) (e^x - 1)/x")
    print("=" * 60)

    def f(x):
        return (math.exp(x) - 1) / x if x != 0 else 1

    lim = Limit(f)

    # This limit equals 1
    result = lim.at(0.0)
    print(f"lim(x→0) (e^x - 1)/x = {result}")
    print("Expected: 1.0")
    print()


def example_7_checking_multiple_points():
    """Example 7: Checking limits at multiple points."""
    print("=" * 60)
    print("Example 7: Continuity check for f(x) = |x|")
    print("=" * 60)

    def f(x):
        return abs(x)

    lim = Limit(f)

    test_points = [-2, -1, 0, 1, 2]

    print("Testing continuity at various points:")
    for x in test_points:
        is_cont = lim.is_continuous(x)
        print(f"  x = {x:2d}: Continuous? {is_cont}")
    print()


if __name__ == "__main__":
    example_1_simple_limit()
    example_2_one_sided_limits()
    example_3_continuity()
    example_4_trigonometric_limit()
    example_5_limit_at_infinity()
    example_6_exponential_limit()
    example_7_checking_multiple_points()

    print("=" * 60)
    print("All limit examples completed!")
    print("=" * 60)
