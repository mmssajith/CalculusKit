"""Partial derivative examples using CalculusKit."""

import math

from calculuskit.partial_derivative.partial_derivative import PartialDerivative


def example_1_simple_function():
    """Example 1: Partial derivatives of f(x, y) = x^2 + y^2."""
    print("=" * 60)
    print("Example 1: Partial derivatives of f(x, y) = x² + y²")
    print("=" * 60)

    def f(x, y):
        return x**2 + y**2

    pdf = PartialDerivative(f)

    point = (2.0, 3.0)

    # df/dx = 2x, at (2, 3) should be 4
    df_dx = pdf.at(point, 0)
    print(f"∂f/∂x at {point} = {df_dx}")
    print(f"Expected: {2 * point[0]}")

    # df/dy = 2y, at (2, 3) should be 6
    df_dy = pdf.at(point, 1)
    print(f"∂f/∂y at {point} = {df_dy}")
    print(f"Expected: {2 * point[1]}")
    print()


def example_2_gradient_vector():
    """Example 2: Computing gradient vector."""
    print("=" * 60)
    print("Example 2: Gradient vector of f(x, y) = x²y + y³")
    print("=" * 60)

    def f(x, y):
        return x**2 * y + y**3

    pdf = PartialDerivative(f)

    point = (1.0, 2.0)

    gradient = pdf.gradient_vector(point)

    print(f"∇f at {point} = {gradient}")
    # df/dx = 2xy, at (1, 2) = 4
    # df/dy = x^2 + 3y^2, at (1, 2) = 1 + 12 = 13
    print(f"Expected: [{2 * point[0] * point[1]}, {point[0] ** 2 + 3 * point[1] ** 2}]")
    print()


def example_3_multivariable_function():
    """Example 3: Three-variable function."""
    print("=" * 60)
    print("Example 3: Partial derivatives of f(x, y, z) = x²y + yz² + xz")
    print("=" * 60)

    def f(x, y, z):
        return x**2 * y + y * z**2 + x * z

    pdf = PartialDerivative(f)

    point = (1.0, 2.0, 3.0)

    print(f"Point: {point}")
    print(f"∂f/∂x = {pdf.at(point, 0):.6f}")  # 2xy + z = 2*1*2 + 3 = 7
    print(f"∂f/∂y = {pdf.at(point, 1):.6f}")  # x^2 + z^2 = 1 + 9 = 10
    print(f"∂f/∂z = {pdf.at(point, 2):.6f}")  # 2yz + x = 2*2*3 + 1 = 13

    gradient = pdf.gradient_vector(point)
    print(f"\nGradient vector: {[f'{g:.6f}' for g in gradient]}")
    print()


def example_4_trigonometric():
    """Example 4: Trigonometric multivariable function."""
    print("=" * 60)
    print("Example 4: f(x, y) = sin(x) * cos(y)")
    print("=" * 60)

    def f(x, y):
        return math.sin(x) * math.cos(y)

    pdf = PartialDerivative(f)

    point = (math.pi / 4, math.pi / 3)

    # df/dx = cos(x) * cos(y)
    df_dx = pdf.at(point, 0)
    expected_dx = math.cos(point[0]) * math.cos(point[1])

    # df/dy = sin(x) * (-sin(y))
    df_dy = pdf.at(point, 1)
    expected_dy = math.sin(point[0]) * (-math.sin(point[1]))

    print("Point: (π/4, π/3)")
    print(f"∂f/∂x = {df_dx:.6f}, Expected: {expected_dx:.6f}")
    print(f"∂f/∂y = {df_dy:.6f}, Expected: {expected_dy:.6f}")
    print()


def example_5_exponential():
    """Example 5: Exponential function."""
    print("=" * 60)
    print("Example 5: f(x, y) = e^(x²+y²)")
    print("=" * 60)

    def f(x, y):
        return math.exp(x**2 + y**2)

    pdf = PartialDerivative(f)

    point = (1.0, 1.0)

    gradient = pdf.gradient_vector(point)

    # df/dx = 2x * e^(x²+y²)
    # df/dy = 2y * e^(x²+y²)
    exp_val = math.exp(point[0] ** 2 + point[1] ** 2)
    expected_gradient = [2 * point[0] * exp_val, 2 * point[1] * exp_val]

    print(f"Point: {point}")
    print(f"Gradient: [{gradient[0]:.6f}, {gradient[1]:.6f}]")
    print(f"Expected: [{expected_gradient[0]:.6f}, {expected_gradient[1]:.6f}]")
    print()


def example_6_directional_derivative():
    """Example 6: Computing directional derivative."""
    print("=" * 60)
    print("Example 6: Directional derivative of f(x, y) = x² + y²")
    print("=" * 60)

    def f(x, y):
        return x**2 + y**2

    pdf = PartialDerivative(f)

    point = (3.0, 4.0)

    # Compute gradient
    gradient = pdf.gradient_vector(point)

    # Direction vector (unit vector in direction (1, 1))
    direction = (1 / math.sqrt(2), 1 / math.sqrt(2))

    # Directional derivative = gradient · direction
    directional_deriv = sum(g * d for g, d in zip(gradient, direction))

    print(f"Point: {point}")
    print(f"Gradient: {gradient}")
    print(f"Direction (unit vector): {direction}")
    print(f"Directional derivative: {directional_deriv:.6f}")
    # Expected: (6, 8) · (1/√2, 1/√2) = 14/√2 ≈ 9.899
    print(f"Expected: {14 / math.sqrt(2):.6f}")
    print()


def example_7_saddle_point():
    """Example 7: Analyzing critical points (saddle point)."""
    print("=" * 60)
    print("Example 7: Critical point analysis of f(x, y) = x² - y²")
    print("=" * 60)

    def f(x, y):
        return x**2 - y**2

    pdf = PartialDerivative(f)

    # Critical point at (0, 0) where gradient = 0
    point = (0.0, 0.0)

    gradient = pdf.gradient_vector(point)
    print(f"Gradient at origin {point}: {gradient}")
    print("This is a saddle point (gradient is zero)")

    # Check gradient at nearby points
    print("\nGradient at nearby points:")
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nearby = (float(dx), float(dy))
        grad = pdf.gradient_vector(nearby)
        print(f"  {nearby}: {grad}")
    print()


def example_8_temperature_distribution():
    """Example 8: Temperature distribution (physics application)."""
    print("=" * 60)
    print("Example 8: Temperature distribution T(x, y) = 100 - x² - y²")
    print("=" * 60)

    def T(x, y):
        """Temperature at point (x, y)."""
        return 100 - x**2 - y**2

    pdf = PartialDerivative(T)

    # Sample points
    points = [(0, 0), (1, 1), (2, 2), (3, 3)]

    print("Position | Temperature | Gradient (rate of change)")
    print("-" * 60)
    for point in points:
        temp = T(*point)
        gradient = pdf.gradient_vector(point)
        print(f"{point} | {temp:11.2f} | [{gradient[0]:6.2f}, {gradient[1]:6.2f}]")
    print()


def example_9_jacobian_matrix():
    """Example 9: Jacobian matrix."""
    print("=" * 60)
    print("Example 9: Jacobian matrix of f(x, y) = x²y")
    print("=" * 60)

    def f(x, y):
        return x**2 * y

    pdf = PartialDerivative(f)

    point = (2.0, 3.0)

    jacobian = pdf.jacobian(point)

    print(f"Point: {point}")
    print("Jacobian matrix (1x2 for single-output function):")
    for row in jacobian:
        print(f"  {[f'{val:.6f}' for val in row]}")
    # df/dx = 2xy = 12, df/dy = x^2 = 4
    print(f"Expected: [[{2 * point[0] * point[1]:.6f}, {point[0] ** 2:.6f}]]")
    print()


def example_10_chain_rule():
    """Example 10: Demonstrating chain rule with composition."""
    print("=" * 60)
    print("Example 10: Chain rule - f(x, y) = (x² + y²)²")
    print("=" * 60)

    def f(x, y):
        """Composition: let u = x² + y², then f = u²."""
        return (x**2 + y**2) ** 2

    pdf = PartialDerivative(f)

    point = (1.0, 2.0)

    gradient = pdf.gradient_vector(point)

    # Using chain rule: df/dx = 2u * du/dx = 2(x²+y²) * 2x = 4x(x²+y²)
    u = point[0] ** 2 + point[1] ** 2
    expected_dx = 4 * point[0] * u
    expected_dy = 4 * point[1] * u

    print(f"Point: {point}")
    print(f"∂f/∂x = {gradient[0]:.6f}, Expected: {expected_dx:.6f}")
    print(f"∂f/∂y = {gradient[1]:.6f}, Expected: {expected_dy:.6f}")
    print()


if __name__ == "__main__":
    example_1_simple_function()
    example_2_gradient_vector()
    example_3_multivariable_function()
    example_4_trigonometric()
    example_5_exponential()
    example_6_directional_derivative()
    example_7_saddle_point()
    example_8_temperature_distribution()
    example_9_jacobian_matrix()
    example_10_chain_rule()

    print("=" * 60)
    print("All partial derivative examples completed!")
    print("=" * 60)
