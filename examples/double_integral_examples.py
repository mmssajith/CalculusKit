"""Double integral examples using CalculusKit."""

import math

from calculuskit.double_integral.double_integral import DoubleIntegral


def example_1_simple_rectangle():
    """Example 1: Double integral of f(x, y) = x * y over [0,1] x [0,1]."""
    print("=" * 60)
    print("Example 1: ∫∫ xy dA over [0,1] × [0,1]")
    print("=" * 60)

    def f(x, y):
        return x * y

    dbl_int = DoubleIntegral(f, n=100)

    result = dbl_int.over(0, 1, 0, 1)

    # Expected: ∫₀¹ ∫₀¹ xy dy dx = ∫₀¹ [xy²/2]₀¹ dx = ∫₀¹ x/2 dx = [x²/4]₀¹ = 1/4
    expected = 0.25

    print(f"Result: {result:.6f}")
    print(f"Expected: {expected:.6f}")
    print(f"Error: {abs(result - expected):.10f}")
    print()


def example_2_constant_function():
    """Example 2: Double integral of a constant function."""
    print("=" * 60)
    print("Example 2: ∫∫ 5 dA over [0,2] × [0,3]")
    print("=" * 60)

    def f(_x, _y):
        return 5.0

    dbl_int = DoubleIntegral(f, n=50)

    result = dbl_int.over(0, 2, 0, 3)

    # Expected: 5 * (2-0) * (3-0) = 5 * 6 = 30
    expected = 30.0

    print(f"Result: {result:.6f}")
    print(f"Expected: {expected:.6f}")
    print("Area of rectangle: 2 × 3 = 6")
    print()


def example_3_polynomial():
    """Example 3: Polynomial function."""
    print("=" * 60)
    print("Example 3: ∫∫ (x² + y²) dA over [0,1] × [0,1]")
    print("=" * 60)

    def f(x, y):
        return x**2 + y**2

    dbl_int = DoubleIntegral(f, n=100)

    result = dbl_int.over(0, 1, 0, 1)

    # Expected: ∫₀¹ ∫₀¹ (x² + y²) dy dx = ∫₀¹ [x²y + y³/3]₀¹ dx
    #         = ∫₀¹ (x² + 1/3) dx = [x³/3 + x/3]₀¹ = 1/3 + 1/3 = 2/3
    expected = 2 / 3

    print(f"Result: {result:.6f}")
    print(f"Expected: {expected:.6f}")
    print(f"Error: {abs(result - expected):.10f}")
    print()


def example_4_different_methods():
    """Example 4: Comparing different integration methods."""
    print("=" * 60)
    print("Example 4: Comparing methods for ∫∫ xy dA over [0,2] × [0,2]")
    print("=" * 60)

    def f(x, y):
        return x * y

    # Expected: ∫₀² ∫₀² xy dy dx = ∫₀² [xy²/2]₀² dx = ∫₀² 2x dx = [x²]₀² = 4
    expected = 4.0

    methods = ["trapezoidal", "simpson", "midpoint"]

    print("Method       | Result   | Error")
    print("-" * 40)
    for method in methods:
        dbl_int = DoubleIntegral(f, n=100, method=method)
        result = dbl_int.over(0, 2, 0, 2)
        error = abs(result - expected)
        print(f"{method:12s} | {result:8.6f} | {error:.10f}")

    print(f"\nExpected: {expected:.6f}")
    print()


def example_5_circular_region_approximation():
    """Example 5: Approximating integral over circular region."""
    print("=" * 60)
    print("Example 5: ∫∫ 1 dA over unit circle (approximate)")
    print("=" * 60)

    def f(x, y):
        # Only integrate where x² + y² ≤ 1
        if x**2 + y**2 <= 1:
            return 1.0
        return 0.0

    dbl_int = DoubleIntegral(f, n=200)

    # Integrate over square [-1, 1] × [-1, 1]
    result = dbl_int.over(-1, 1, -1, 1)

    # Expected: Area of unit circle = π
    expected = math.pi

    print(f"Result: {result:.6f}")
    print(f"Expected (π): {expected:.6f}")
    print(f"Error: {abs(result - expected):.6f}")
    print(f"Relative error: {abs(result - expected) / expected * 100:.2f}%")
    print()


def example_6_volume_under_surface():
    """Example 6: Computing volume under a surface."""
    print("=" * 60)
    print("Example 6: Volume under z = 4 - x² - y² over [0,1] × [0,1]")
    print("=" * 60)

    def f(x, y):
        return 4 - x**2 - y**2

    dbl_int = DoubleIntegral(f, n=100)

    volume = dbl_int.over(0, 1, 0, 1)

    # Expected: ∫₀¹ ∫₀¹ (4 - x² - y²) dy dx
    #         = ∫₀¹ [4y - x²y - y³/3]₀¹ dx
    #         = ∫₀¹ (4 - x² - 1/3) dx
    #         = ∫₀¹ (11/3 - x²) dx
    #         = [11x/3 - x³/3]₀¹ = 11/3 - 1/3 = 10/3
    expected = 10 / 3

    print(f"Volume: {volume:.6f}")
    print(f"Expected: {expected:.6f}")
    print(f"Error: {abs(volume - expected):.10f}")
    print()


def example_7_exponential_function():
    """Example 7: Exponential function."""
    print("=" * 60)
    print("Example 7: ∫∫ e^(x+y) dA over [0,1] × [0,1]")
    print("=" * 60)

    def f(x, y):
        return math.exp(x + y)

    dbl_int = DoubleIntegral(f, n=100)

    result = dbl_int.over(0, 1, 0, 1)

    # Expected: ∫₀¹ ∫₀¹ e^(x+y) dy dx = ∫₀¹ [e^(x+y)]₀¹ dx
    #         = ∫₀¹ (e^(x+1) - e^x) dx = ∫₀¹ e^x(e - 1) dx
    #         = (e - 1)[e^x]₀¹ = (e - 1)(e - 1) = (e - 1)²
    expected = (math.e - 1) ** 2

    print(f"Result: {result:.6f}")
    print(f"Expected ((e-1)²): {expected:.6f}")
    print(f"Error: {abs(result - expected):.10f}")
    print()


def example_8_trigonometric():
    """Example 8: Trigonometric function."""
    print("=" * 60)
    print("Example 8: ∫∫ sin(x) * cos(y) dA over [0,π] × [0,π]")
    print("=" * 60)

    def f(x, y):
        return math.sin(x) * math.cos(y)

    dbl_int = DoubleIntegral(f, n=200)

    result = dbl_int.over(0, math.pi, 0, math.pi)

    # Expected: ∫₀^π ∫₀^π sin(x)cos(y) dy dx
    #         = ∫₀^π sin(x)[sin(y)]₀^π dx = ∫₀^π sin(x) * 0 dx = 0
    expected = 0.0

    print(f"Result: {result:.10f}")
    print(f"Expected: {expected:.6f}")
    print(f"Error: {abs(result - expected):.10f}")
    print()


def example_9_average_value():
    """Example 9: Computing average value over a region."""
    print("=" * 60)
    print("Example 9: Average value of f(x,y) = x² + y² over [0,2] × [0,2]")
    print("=" * 60)

    def f(x, y):
        return x**2 + y**2

    dbl_int = DoubleIntegral(f, n=100)

    # Calculate double integral
    integral_value = dbl_int.over(0, 2, 0, 2)

    # Area of region
    area = (2 - 0) * (2 - 0)

    # Average value = (1/Area) * ∫∫ f dA
    average = integral_value / area

    print(f"Double integral: {integral_value:.6f}")
    print(f"Area of region: {area:.6f}")
    print(f"Average value: {average:.6f}")

    # Expected: ∫₀² ∫₀² (x² + y²) dy dx = ∫₀² [x²y + y³/3]₀² dx
    #         = ∫₀² (2x² + 8/3) dx = [2x³/3 + 8x/3]₀² = 16/3 + 16/3 = 32/3
    # Average = (32/3) / 4 = 8/3
    expected = 8 / 3
    print(f"Expected average: {expected:.6f}")
    print()


def example_10_mass_density():
    """Example 10: Computing mass from density function."""
    print("=" * 60)
    print("Example 10: Mass of plate with density ρ(x,y) = x + y")
    print("=" * 60)

    def density(x, y):
        """Density function: ρ(x, y) = x + y kg/m²."""
        return x + y

    dbl_int = DoubleIntegral(density, n=100)

    # Mass over region [0,3] × [0,2]
    mass = dbl_int.over(0, 3, 0, 2)

    # Expected: ∫₀³ ∫₀² (x + y) dy dx = ∫₀³ [xy + y²/2]₀² dx
    #         = ∫₀³ (2x + 2) dx = [x² + 2x]₀³ = 9 + 6 = 15
    expected = 15.0

    print("Region: [0,3] × [0,2]")
    print("Density function: ρ(x,y) = x + y")
    print(f"Total mass: {mass:.6f} kg")
    print(f"Expected: {expected:.6f} kg")
    print(f"Error: {abs(mass - expected):.10f}")
    print()


def example_11_moment_calculation():
    """Example 11: Moment calculation for center of mass."""
    print("=" * 60)
    print("Example 11: First moment Mx for uniform plate over [0,2] × [0,2]")
    print("=" * 60)

    # For uniform density ρ = 1, Mx = ∫∫ y dA
    def integrand_mx(_x, y):
        return y  # y * ρ where ρ = 1

    dbl_int = DoubleIntegral(integrand_mx, n=100)

    # Calculate Mx (moment about x-axis)
    Mx = dbl_int.over(0, 2, 0, 2)

    # Mass (for uniform density)
    mass_dbl_int = DoubleIntegral(lambda _x, _y: 1.0, n=100)
    mass = mass_dbl_int.over(0, 2, 0, 2)

    # y-coordinate of center of mass
    y_bar = Mx / mass

    # Expected: Mx = ∫₀² ∫₀² y dy dx = ∫₀² [y²/2]₀² dx = ∫₀² 2 dx = 4
    # Mass = 4 (area), y_bar = 4/4 = 1 (center at y = 1)
    expected_Mx = 4.0
    expected_y_bar = 1.0

    print(f"Moment Mx: {Mx:.6f}")
    print(f"Expected Mx: {expected_Mx:.6f}")
    print(f"Mass: {mass:.6f}")
    print(f"Center of mass (y-coordinate): {y_bar:.6f}")
    print(f"Expected y-coordinate: {expected_y_bar:.6f}")
    print()


def example_12_gaussian_surface():
    """Example 12: Gaussian (bell curve) surface."""
    print("=" * 60)
    print("Example 12: Volume under Gaussian z = e^(-(x²+y²))")
    print("=" * 60)

    def f(x, y):
        return math.exp(-(x**2 + y**2))

    dbl_int = DoubleIntegral(f, n=150)

    # Integrate over [-2, 2] × [-2, 2]
    volume = dbl_int.over(-2, 2, -2, 2)

    # Analytical: ∫∫ e^(-(x²+y²)) dA over entire plane = π
    # Over [-2,2]×[-2,2] we get approximately 3.1398
    print(f"Volume (over [-2,2] × [-2,2]): {volume:.6f}")
    print(f"Note: Over entire plane, the integral equals π ≈ {math.pi:.6f}")
    print(f"Percentage captured: {volume / math.pi * 100:.2f}%")
    print()


if __name__ == "__main__":
    example_1_simple_rectangle()
    example_2_constant_function()
    example_3_polynomial()
    example_4_different_methods()
    example_5_circular_region_approximation()
    example_6_volume_under_surface()
    example_7_exponential_function()
    example_8_trigonometric()
    example_9_average_value()
    example_10_mass_density()
    example_11_moment_calculation()
    example_12_gaussian_surface()

    print("=" * 60)
    print("All double integral examples completed!")
    print("=" * 60)
