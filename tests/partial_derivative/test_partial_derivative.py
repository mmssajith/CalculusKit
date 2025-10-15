"""Test cases for PartialDerivative class."""

import math

from calculuskit.partial_derivative.partial_derivative import PartialDerivative


def test_partial_derivative_sum():
    """Test partial derivative of f(x, y) = x^2 + y^2."""

    def f(x, y):
        return x**2 + y**2

    pdf = PartialDerivative(f)

    # df/dx at (2, 3) should be 2*x = 4
    assert abs(pdf.at((2.0, 3.0), 0) - 4.0) < 1e-5

    # df/dy at (2, 3) should be 2*y = 6
    assert abs(pdf.at((2.0, 3.0), 1) - 6.0) < 1e-5


def test_partial_derivative_product():
    """Test partial derivative of f(x, y) = x * y."""

    def f(x, y):
        return x * y

    pdf = PartialDerivative(f)

    # df/dx at (2, 3) should be y = 3
    assert abs(pdf.at((2.0, 3.0), 0) - 3.0) < 1e-5

    # df/dy at (2, 3) should be x = 2
    assert abs(pdf.at((2.0, 3.0), 1) - 2.0) < 1e-5


def test_partial_derivative_three_variables():
    """Test partial derivative with three variables."""

    def f(x, y, z):
        return x**2 + y**2 + z**2

    pdf = PartialDerivative(f)

    # df/dx at (1, 2, 3) should be 2*x = 2
    assert abs(pdf.at((1.0, 2.0, 3.0), 0) - 2.0) < 1e-5

    # df/dy at (1, 2, 3) should be 2*y = 4
    assert abs(pdf.at((1.0, 2.0, 3.0), 1) - 4.0) < 1e-5

    # df/dz at (1, 2, 3) should be 2*z = 6
    assert abs(pdf.at((1.0, 2.0, 3.0), 2) - 6.0) < 1e-5


def test_gradient_vector():
    """Test gradient vector calculation."""

    def f(x, y):
        return x**2 + y**2

    pdf = PartialDerivative(f)
    gradient = pdf.gradient_vector((2.0, 3.0))

    assert len(gradient) == 2
    assert abs(gradient[0] - 4.0) < 1e-5
    assert abs(gradient[1] - 6.0) < 1e-5


def test_jacobian():
    """Test Jacobian matrix calculation."""

    def f(x, y):
        return x**2 + y**2

    pdf = PartialDerivative(f)
    jacobian = pdf.jacobian((2.0, 3.0))

    assert len(jacobian) == 1
    assert len(jacobian[0]) == 2
    assert abs(jacobian[0][0] - 4.0) < 1e-5
    assert abs(jacobian[0][1] - 6.0) < 1e-5


def test_partial_derivative_trig():
    """Test partial derivative with trigonometric functions."""

    def f(x, y):
        return math.sin(x) * math.cos(y)

    pdf = PartialDerivative(f)

    # df/dx at (0, 0) should be cos(0) * cos(0) = 1
    assert abs(pdf.at((0.0, 0.0), 0) - 1.0) < 1e-5

    # df/dy at (0, 0) should be sin(0) * (-sin(0)) = 0
    assert abs(pdf.at((0.0, 0.0), 1)) < 1e-5
