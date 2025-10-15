"""Maclaurin series examples using CalculusKit."""

import math

from calculuskit.maclaurin_series.maclaurin_series import MaclaurinSeries


def example_1_exponential():
    """Example 1: Maclaurin series for e^x."""
    print("=" * 60)
    print("Example 1: Maclaurin series for e^x")
    print("=" * 60)

    def f(x):
        return math.exp(x)

    maclaurin = MaclaurinSeries(f, n=10)

    # Test at x = 1
    x = 1.0
    result = maclaurin.at(x)
    expected = math.e

    print(f"Maclaurin approximation at x={x}: {result:.10f}")
    print(f"Actual value e: {expected:.10f}")
    print(f"Error: {abs(result - expected):.10f}")
    print()


def example_2_sine():
    """Example 2: Maclaurin series for sin(x)."""
    print("=" * 60)
    print("Example 2: Maclaurin series for sin(x)")
    print("=" * 60)

    def f(x):
        return math.sin(x)

    maclaurin = MaclaurinSeries(f, n=15)

    # Test at various points
    print("x   | sin(x)   | Maclaurin | Error")
    print("-" * 50)

    for x in [0.5, 1.0, 1.5, 2.0]:
        result = maclaurin.at(x)
        expected = math.sin(x)
        error = abs(result - expected)
        print(f"{x:3.1f} | {expected:8.6f} | {result:9.6f} | {error:.10f}")

    print()


def example_3_cosine():
    """Example 3: Maclaurin series for cos(x)."""
    print("=" * 60)
    print("Example 3: Maclaurin series for cos(x)")
    print("=" * 60)

    def f(x):
        return math.cos(x)

    maclaurin = MaclaurinSeries(f, n=15)

    # Test at various points
    print("x   | cos(x)   | Maclaurin | Error")
    print("-" * 50)

    for x in [0, 0.5, 1.0, math.pi / 4, math.pi / 2]:
        result = maclaurin.at(x)
        expected = math.cos(x)
        error = abs(result - expected)
        print(f"{x:3.3f} | {expected:8.6f} | {result:9.6f} | {error:.10f}")

    print()


def example_4_polynomial_representation():
    """Example 4: Polynomial string representation."""
    print("=" * 60)
    print("Example 4: Polynomial representation of e^x")
    print("=" * 60)

    def f(x):
        return math.exp(x)

    maclaurin = MaclaurinSeries(f, n=6)

    poly_str = maclaurin.polynomial_string()
    print("Maclaurin polynomial for e^x:")
    print(poly_str)
    print()

    # Known series: e^x = 1 + x + x²/2! + x³/3! + x⁴/4! + ...
    print("Known series: e^x = 1 + x + x²/2! + x³/3! + x⁴/4! + ...")
    print()


def example_5_coefficients():
    """Example 5: Extract Maclaurin coefficients."""
    print("=" * 60)
    print("Example 5: Maclaurin coefficients for sin(x)")
    print("=" * 60)

    def f(x):
        return math.sin(x)

    maclaurin = MaclaurinSeries(f, n=10)

    coeffs = maclaurin.coefficients()

    print("Maclaurin coefficients:")
    for i, coeff in enumerate(coeffs):
        if abs(coeff) > 1e-10:
            print(f"  c_{i} (x^{i}): {coeff:12.8f}")

    print()
    print("Known pattern for sin(x):")
    print("  Odd terms: (-1)^k / (2k+1)! for k=0,1,2,...")
    print("  Even terms: 0")
    print()


def example_6_logarithm():
    """Example 6: Maclaurin series for ln(1+x)."""
    print("=" * 60)
    print("Example 6: Maclaurin series for ln(1+x)")
    print("=" * 60)

    def f(x):
        return math.log(1 + x)

    maclaurin = MaclaurinSeries(f, n=20)

    # Test for -0.5 < x < 1 (convergence region)
    print("x    | ln(1+x)  | Maclaurin | Error")
    print("-" * 50)

    for x in [0.1, 0.2, 0.3, 0.5]:
        result = maclaurin.at(x)
        expected = math.log(1 + x)
        error = abs(result - expected)
        print(f"{x:4.1f} | {expected:8.6f} | {result:9.6f} | {error:.10f}")

    print()


def example_7_convergence_rate():
    """Example 7: Analyzing convergence with increasing terms."""
    print("=" * 60)
    print("Example 7: Convergence analysis for e^x at x=1")
    print("=" * 60)

    def f(x):
        return math.exp(x)

    x = 1.0
    expected = math.e

    print("n terms | Approximation | Error")
    print("-" * 45)

    for n in [3, 5, 10, 15, 20]:
        maclaurin = MaclaurinSeries(f, n=n)
        result = maclaurin.at(x)
        error = abs(result - expected)
        print(f"{n:7d} | {result:13.10f} | {error:.10e}")

    print(f"\nActual value e: {expected:.10f}")
    print()


def example_8_arctan():
    """Example 8: Maclaurin series for arctan(x)."""
    print("=" * 60)
    print("Example 8: Maclaurin series for arctan(x)")
    print("=" * 60)

    def f(x):
        return math.atan(x)

    maclaurin = MaclaurinSeries(f, n=20)

    # Works well for |x| < 1
    print("x    | arctan(x) | Maclaurin | Error")
    print("-" * 50)

    for x in [0.1, 0.3, 0.5, 0.7]:
        result = maclaurin.at(x)
        expected = math.atan(x)
        error = abs(result - expected)
        print(f"{x:4.1f} | {expected:9.6f} | {result:9.6f} | {error:.10f}")

    print()


def example_9_hyperbolic_sine():
    """Example 9: Maclaurin series for sinh(x)."""
    print("=" * 60)
    print("Example 9: Maclaurin series for sinh(x)")
    print("=" * 60)

    def f(x):
        return math.sinh(x)

    maclaurin = MaclaurinSeries(f, n=15)

    print("x   | sinh(x)  | Maclaurin | Error")
    print("-" * 50)

    for x in [0.5, 1.0, 1.5, 2.0]:
        result = maclaurin.at(x)
        expected = math.sinh(x)
        error = abs(result - expected)
        print(f"{x:3.1f} | {expected:8.6f} | {result:9.6f} | {error:.10f}")

    print()


def example_10_hyperbolic_cosine():
    """Example 10: Maclaurin series for cosh(x)."""
    print("=" * 60)
    print("Example 10: Maclaurin series for cosh(x)")
    print("=" * 60)

    def f(x):
        return math.cosh(x)

    maclaurin = MaclaurinSeries(f, n=15)

    print("x   | cosh(x)  | Maclaurin | Error")
    print("-" * 50)

    for x in [0, 0.5, 1.0, 1.5]:
        result = maclaurin.at(x)
        expected = math.cosh(x)
        error = abs(result - expected)
        print(f"{x:3.1f} | {expected:8.6f} | {result:9.6f} | {error:.10f}")

    print()


def example_11_comparing_series():
    """Example 11: Comparing e^x, sinh(x), and cosh(x) series."""
    print("=" * 60)
    print("Example 11: Relationship between e^x, sinh(x), cosh(x)")
    print("Identity: e^x = cosh(x) + sinh(x)")
    print("=" * 60)

    def exp_func(x):
        return math.exp(x)

    def sinh_func(x):
        return math.sinh(x)

    def cosh_func(x):
        return math.cosh(x)

    exp_series = MaclaurinSeries(exp_func, n=12)
    sinh_series = MaclaurinSeries(sinh_func, n=12)
    cosh_series = MaclaurinSeries(cosh_func, n=12)

    x = 1.0

    exp_val = exp_series.at(x)
    sinh_val = sinh_series.at(x)
    cosh_val = cosh_series.at(x)

    print(f"At x = {x}:")
    print(f"  e^x:             {exp_val:.10f}")
    print(f"  cosh(x) + sinh(x): {cosh_val + sinh_val:.10f}")
    print(f"  Difference:      {abs(exp_val - (cosh_val + sinh_val)):.10e}")
    print()


def example_12_radius_of_convergence():
    """Example 12: Demonstrating radius of convergence."""
    print("=" * 60)
    print("Example 12: Radius of convergence for 1/(1-x)")
    print("Converges for |x| < 1")
    print("=" * 60)

    def f(x):
        return 1 / (1 - x)

    maclaurin = MaclaurinSeries(f, n=20)

    print("Testing approximation quality at different x values:")
    print("x    | f(x)     | Maclaurin | Error")
    print("-" * 50)

    # Inside convergence radius
    for x in [0.2, 0.5, 0.8]:
        result = maclaurin.at(x)
        expected = f(x)
        error = abs(result - expected)
        print(f"{x:4.1f} | {expected:8.4f} | {result:9.4f} | {error:.6f}")

    print("\nOutside convergence radius (x >= 1):")
    print("Series diverges, approximation poor:")
    for x in [1.1, 1.5]:
        result = maclaurin.at(x)
        expected = f(x)
        print(f"{x:4.1f} | {expected:8.4f} | {result:9.4f} | (divergent)")

    print()


def example_13_error_estimation():
    """Example 13: Error estimation for Maclaurin series."""
    print("=" * 60)
    print("Example 13: Error estimation for sin(x)")
    print("=" * 60)

    def f(x):
        return math.sin(x)

    x = 1.0

    print(f"Approximating sin({x}):")
    print("n terms | Approximation | Actual Error | Estimated Error")
    print("-" * 65)

    for n in [5, 10, 15, 20]:
        maclaurin = MaclaurinSeries(f, n=n)
        result = maclaurin.at(x)
        actual_error = abs(result - math.sin(x))
        estimated_error = maclaurin.error_estimate(x)

        print(f"{n:7d} | {result:13.10f} | {actual_error:12.10e} | {estimated_error:15.10e}")

    print()


def example_14_polynomial_approximation():
    """Example 14: Using Maclaurin series for polynomial approximation."""
    print("=" * 60)
    print("Example 14: Approximating sin(x) near x=0")
    print("=" * 60)

    def f(x):
        return math.sin(x)

    # Low-order approximation
    maclaurin_low = MaclaurinSeries(f, n=3)
    poly_low = maclaurin_low.polynomial_string()

    print("Low-order approximation (n=3):")
    print(poly_low)
    print()

    # Test near x=0 where approximation is best
    print("Testing near x=0:")
    print("x     | sin(x)   | n=3      | n=10     ")
    print("-" * 50)

    maclaurin_high = MaclaurinSeries(f, n=10)

    for x in [0.1, 0.2, 0.3, 0.5]:
        actual = math.sin(x)
        approx_low = maclaurin_low.at(x)
        approx_high = maclaurin_high.at(x)
        print(f"{x:5.2f} | {actual:8.6f} | {approx_low:8.6f} | {approx_high:8.6f}")

    print()


def example_15_special_values():
    """Example 15: Computing special values using Maclaurin series."""
    print("=" * 60)
    print("Example 15: Computing π/4 using arctan(1)")
    print("Using: π/4 = arctan(1)")
    print("=" * 60)

    def f(x):
        return math.atan(x)

    # arctan converges slowly at x=1, so use many terms
    maclaurin = MaclaurinSeries(f, n=100)

    result = maclaurin.at(1.0)
    expected = math.pi / 4

    print(f"arctan(1) via Maclaurin (n=100): {result:.10f}")
    print(f"Actual π/4:                      {expected:.10f}")
    print(f"Error:                           {abs(result - expected):.10e}")
    print()
    print("Note: Better to use arctan(1/√3) = π/6 for faster convergence")
    print()


if __name__ == "__main__":
    example_1_exponential()
    example_2_sine()
    example_3_cosine()
    example_4_polynomial_representation()
    example_5_coefficients()
    example_6_logarithm()
    example_7_convergence_rate()
    example_8_arctan()
    example_9_hyperbolic_sine()
    example_10_hyperbolic_cosine()
    example_11_comparing_series()
    example_12_radius_of_convergence()
    example_13_error_estimation()
    example_14_polynomial_approximation()
    example_15_special_values()

    print("=" * 60)
    print("All Maclaurin series examples completed!")
    print("=" * 60)
