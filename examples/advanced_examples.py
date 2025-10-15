"""Advanced examples combining multiple CalculusKit features."""

import math

from calculuskit.derivative.derivative import Derivative
from calculuskit.integral.integral import Integral
from calculuskit.taylor_series.taylor_series import TaylorSeries


def example_1_fundamental_theorem():
    """Example 1: Fundamental Theorem of Calculus."""
    print("=" * 60)
    print("Example 1: Fundamental Theorem of Calculus")
    print("Verifying: d/dx[∫ₐˣ f(t)dt] = f(x)")
    print("=" * 60)

    # Define function f(x) = x^2
    def f(x):
        return x**2

    # Create integral F(x) = ∫₀ˣ t² dt = x³/3
    integral = Integral(f)

    # Define F(x) as the integral from 0 to x
    def F(x):
        return integral.between(0, x)

    # Take derivative of F(x)
    dF = Derivative(F)

    # Test at x = 2
    x = 2.0
    derivative_of_integral = dF.at(x)
    original_function = f(x)

    print("f(x) = x²")
    print("F(x) = ∫₀ˣ t² dt")
    print(f"At x = {x}:")
    print(f"  F'(x) = {derivative_of_integral:.6f}")
    print(f"  f(x) = {original_function:.6f}")
    print(f"  Difference: {abs(derivative_of_integral - original_function):.10f}")
    print()


def example_2_optimization():
    """Example 2: Finding local maxima/minima using derivatives."""
    print("=" * 60)
    print("Example 2: Finding extrema of f(x) = x³ - 3x² + 2")
    print("=" * 60)

    def f(x):
        return x**3 - 3 * x**2 + 2

    # First derivative
    df = Derivative(f)

    # Search for critical points where f'(x) ≈ 0
    print("Searching for critical points where f'(x) = 0:")
    critical_points = []
    for x in [i * 0.1 for i in range(-20, 50)]:
        deriv = df.at(x)
        if abs(deriv) < 0.1:  # Close to zero
            critical_points.append(x)

    # Remove duplicates (keep points that are far apart)
    unique_critical = []
    for cp in critical_points:
        if not unique_critical or abs(cp - unique_critical[-1]) > 0.5:
            unique_critical.append(cp)

    # Check second derivative to classify
    for cp in unique_critical:
        # Second derivative using derivative of derivative
        def df_func(x):
            return df.at(x)

        d2f = Derivative(df_func)
        second_deriv = d2f.at(cp)

        classification = "local minimum" if second_deriv > 0 else "local maximum"
        print(f"  x = {cp:.2f}: f(x) = {f(cp):.4f}, f''(x) = {second_deriv:.4f} ({classification})")
    print()


def example_3_arc_length():
    """Example 3: Computing arc length of a curve."""
    print("=" * 60)
    print("Example 3: Arc length of f(x) = x² from x=0 to x=1")
    print("Arc length formula: L = ∫ₐᵇ √(1 + (f'(x))²) dx")
    print("=" * 60)

    def f(x):
        return x**2

    # Get derivative
    df = Derivative(f)

    # Arc length integrand: √(1 + (f'(x))²)
    def arc_length_integrand(x):
        deriv = df.at(x)
        return math.sqrt(1 + deriv**2)

    # Compute arc length
    integral = Integral(arc_length_integrand, n=2000)
    arc_length = integral.between(0, 1)

    print(f"Arc length: {arc_length:.6f}")
    # Analytical solution for comparison: approximately 1.4789
    print("Expected (analytical): ~1.4789")
    print()


def example_4_rate_of_change():
    """Example 4: Analyzing rate of change."""
    print("=" * 60)
    print("Example 4: Population growth P(t) = 1000e^(0.1t)")
    print("=" * 60)

    def P(t):
        return 1000 * math.exp(0.1 * t)

    # Rate of change
    dP = Derivative(P)

    print("Time (years) | Population | Growth Rate")
    print("-" * 50)
    for t in [0, 5, 10, 15, 20]:
        pop = P(t)
        rate = dP.at(t)
        print(f"{t:12.0f} | {pop:10.0f} | {rate:11.2f}")
    print()


def example_5_work_and_energy():
    """Example 5: Computing work done (physics application)."""
    print("=" * 60)
    print("Example 5: Work done by force F(x) = x² from x=0 to x=5")
    print("Work = ∫ₐᵇ F(x) dx")
    print("=" * 60)

    # Force as a function of position
    def F(x):
        return x**2

    integral = Integral(F, n=1000)

    work = integral.between(0, 5)

    print(f"Work done: {work:.4f} Joules")
    print(f"Expected (x³/3 from 0 to 5): {5**3 / 3:.4f} Joules")
    print()


def example_6_taylor_approximation_error():
    """Example 6: Using Taylor series with error analysis."""
    print("=" * 60)
    print("Example 6: Taylor approximation of sin(x) near π/4")
    print("=" * 60)

    def f(x):
        return math.sin(x)

    center = math.pi / 4
    taylor = TaylorSeries(f, n=5)

    print(f"Taylor series centered at x = π/4 ≈ {center:.4f}")
    print()
    print("x value | Actual | Taylor | Error")
    print("-" * 60)

    for offset in [-0.2, -0.1, 0, 0.1, 0.2]:
        x = center + offset
        actual = math.sin(x)
        approx = taylor.at(x, center)
        error = abs(actual - approx)
        print(f"{x:7.4f} | {actual:6.4f} | {approx:6.4f} | {error:.8f}")
    print()


def example_7_related_rates():
    """Example 7: Related rates problem."""
    print("=" * 60)
    print("Example 7: Related rates - expanding circle")
    print("If radius increases at 2 cm/s, how fast is area increasing?")
    print("=" * 60)

    # Area as function of radius: A = πr²
    def A(r):
        return math.pi * r**2

    # dA/dr
    dA = Derivative(A)

    # Given dr/dt = 2 cm/s, find dA/dt = (dA/dr) * (dr/dt)
    dr_dt = 2.0  # cm/s

    print("Radius (cm) | dA/dr (cm) | dA/dt (cm²/s)")
    print("-" * 50)
    for r in [1, 2, 3, 4, 5]:
        dA_dr = dA.at(r)
        dA_dt = dA_dr * dr_dt
        print(f"{r:11.0f} | {dA_dr:10.4f} | {dA_dt:13.4f}")
    print()


def example_8_numerical_vs_analytical():
    """Example 8: Comparing numerical and analytical results."""
    print("=" * 60)
    print("Example 8: Numerical vs Analytical - f(x) = x³")
    print("=" * 60)

    def f(x):
        return x**3

    # Analytical derivative: f'(x) = 3x²
    def analytical_derivative(x):
        return 3 * x**2

    # Numerical derivative
    df = Derivative(f)

    print("Testing derivative:")
    print("x | Numerical | Analytical | Error")
    print("-" * 50)
    for x in [0, 1, 2, 3, 4, 5]:
        num = df.at(x)
        ana = analytical_derivative(x)
        error = abs(num - ana)
        print(f"{x} | {num:9.6f} | {ana:10.6f} | {error:.10e}")
    print()

    # Analytical integral: ∫x³dx = x⁴/4
    def analytical_integral(a, b):
        return (b**4 - a**4) / 4

    # Numerical integral
    integral = Integral(f, n=1000)

    print("Testing integral from 0 to 5:")
    num_int = integral.between(0, 5)
    ana_int = analytical_integral(0, 5)
    error_int = abs(num_int - ana_int)
    print(f"Numerical:  {num_int:.6f}")
    print(f"Analytical: {ana_int:.6f}")
    print(f"Error:      {error_int:.10e}")
    print()


if __name__ == "__main__":
    example_1_fundamental_theorem()
    example_2_optimization()
    example_3_arc_length()
    example_4_rate_of_change()
    example_5_work_and_energy()
    example_6_taylor_approximation_error()
    example_7_related_rates()
    example_8_numerical_vs_analytical()

    print("=" * 60)
    print("All advanced examples completed!")
    print("=" * 60)
