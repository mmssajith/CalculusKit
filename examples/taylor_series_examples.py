"""Taylor series examples using CalculusKit."""

import math

from calculuskit.taylor_series.taylor_series import TaylorSeries


def example_1_exponential():
    """Example 1: Taylor series for e^x."""
    print("=" * 60)
    print("Example 1: Taylor series for f(x) = e^x around x=0")
    print("=" * 60)

    def f(x):
        return math.exp(x)

    # Create Taylor series with 10 terms
    taylor = TaylorSeries(f, n=10)

    # Evaluate at x=1
    x = 1.0
    result = taylor.at(x, center=0)
    expected = math.exp(x)

    print(f"Taylor approximation at x={x}: {result}")
    print(f"Actual value e^{x}: {expected}")
    print(f"Error: {abs(result - expected):.10f}")
    print()


def example_2_sine_function():
    """Example 2: Taylor series for sin(x)."""
    print("=" * 60)
    print("Example 2: Taylor series for f(x) = sin(x) around x=0")
    print("=" * 60)

    def f(x):
        return math.sin(x)

    taylor = TaylorSeries(f, n=15)

    # Test at π/4
    x = math.pi / 4
    result = taylor.at(x, center=0)
    expected = math.sin(x)

    print(f"Taylor approximation at x=π/4: {result}")
    print(f"Actual value sin(π/4): {expected}")
    print(f"Error: {abs(result - expected):.10f}")
    print()


def example_3_polynomial_string():
    """Example 3: Generate polynomial string representation."""
    print("=" * 60)
    print("Example 3: Polynomial representation of e^x")
    print("=" * 60)

    def f(x):
        return math.exp(x)

    taylor = TaylorSeries(f, n=6)

    # Get string representation
    poly_str = taylor.polynomial_string(center=0)
    print("Taylor polynomial:")
    print(poly_str)
    print()


def example_4_different_centers():
    """Example 4: Taylor series with different center points."""
    print("=" * 60)
    print("Example 4: Taylor series for ln(x) at different centers")
    print("=" * 60)

    def f(x):
        return math.log(x)

    taylor = TaylorSeries(f, n=10)

    # Expand around x=1
    print("Expanding around x=1:")
    x = 1.5
    result1 = taylor.at(x, center=1.0)
    actual = math.log(x)
    print(f"  Taylor approximation at x={x}: {result1}")
    print(f"  Actual value ln({x}): {actual}")
    print(f"  Error: {abs(result1 - actual):.10f}")
    print()

    # Expand around x=2
    print("Expanding around x=2:")
    result2 = taylor.at(x, center=2.0)
    print(f"  Taylor approximation at x={x}: {result2}")
    print(f"  Actual value ln({x}): {actual}")
    print(f"  Error: {abs(result2 - actual):.10f}")
    print()


def example_5_coefficients():
    """Example 5: Extract Taylor series coefficients."""
    print("=" * 60)
    print("Example 5: Taylor series coefficients for cos(x)")
    print("=" * 60)

    def f(x):
        return math.cos(x)

    taylor = TaylorSeries(f, n=8)

    coeffs = taylor.coefficients(center=0)

    print("Taylor series coefficients:")
    for i, coeff in enumerate(coeffs):
        if abs(coeff) > 1e-10:  # Only show non-zero coefficients
            print(f"  a_{i} = {coeff:10.6f}")
    print()


def example_6_error_estimation():
    """Example 6: Error estimation in Taylor approximation."""
    print("=" * 60)
    print("Example 6: Error estimation for different numbers of terms")
    print("=" * 60)

    def f(x):
        return math.exp(x)

    x = 2.0
    actual = math.exp(x)

    print(f"Approximating e^{x} = {actual:.10f}")
    print()
    print("n_terms | Approximation | Error")
    print("-" * 50)

    for n in [3, 5, 10, 15, 20]:
        taylor = TaylorSeries(f, n=n)
        approx = taylor.at(x, center=0)
        error = abs(approx - actual)
        print(f"{n:7d} | {approx:13.10f} | {error:.10e}")
    print()


def example_7_comparison():
    """Example 7: Comparing Taylor series at different points."""
    print("=" * 60)
    print("Example 7: Taylor series accuracy at different distances")
    print("=" * 60)

    def f(x):
        return math.exp(x)

    taylor = TaylorSeries(f, n=10)
    center = 0.0

    print(f"Taylor series for e^x centered at x={center} with {taylor.n} terms")
    print()
    print("Distance from center | x value | Error")
    print("-" * 60)

    for distance in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
        x = center + distance
        approx = taylor.at(x, center)
        actual = math.exp(x)
        error = abs(approx - actual)
        print(f"{distance:18.1f} | {x:7.1f} | {error:.10e}")
    print()


def example_8_custom_function():
    """Example 8: Taylor series for custom function."""
    print("=" * 60)
    print("Example 8: Taylor series for f(x) = 1/(1+x)")
    print("=" * 60)

    def f(x):
        return 1 / (1 + x)

    taylor = TaylorSeries(f, n=8)

    # Show polynomial
    poly_str = taylor.polynomial_string(center=0)
    print("Taylor polynomial:")
    print(poly_str)
    print()

    # Test accuracy
    x = 0.5
    result = taylor.at(x, center=0)
    expected = f(x)

    print(f"At x={x}:")
    print(f"  Taylor approximation: {result}")
    print(f"  Actual value: {expected}")
    print(f"  Error: {abs(result - expected):.10f}")
    print()


if __name__ == "__main__":
    example_1_exponential()
    example_2_sine_function()
    example_3_polynomial_string()
    example_4_different_centers()
    example_5_coefficients()
    example_6_error_estimation()
    example_7_comparison()
    example_8_custom_function()

    print("=" * 60)
    print("All Taylor series examples completed!")
    print("=" * 60)
