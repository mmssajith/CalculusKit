# CalculusKit

A comprehensive Python library for mathematical calculus operations including derivatives, integrals, limits, series expansions, and visualization tools.

## Features

### Core Operations
- **Derivatives**: Numerical differentiation with multiple methods (forward, backward, central)
- **Partial Derivatives**: Support for multivariable functions with gradient vectors and Jacobian matrices
- **Integration**: Numerical integration using trapezoidal, Simpson's, and midpoint rules
- **Double Integrals**: Two-dimensional integration over rectangular regions
- **Limits**: Calculate limits from left, right, or both directions, including limits at infinity
- **Series Expansions**: Taylor series, Maclaurin series, and Fourier series

### Visualization
- **2D Plotting**: Line plots, multiple functions, parametric plots, polar plots, and scatter plots
- **3D Plotting**: Surface plots, contour plots, and wireframe plots
- **Vector Fields**: Quiver plots for visualizing 2D vector fields
- **Animations**: Series approximation convergence and limit behavior animations
- Requires: `matplotlib` (included in dependencies)

## Package Structure

```
calculuskit/
├── derivative/         # Derivative calculations
├── partial_derivative/ # Partial derivatives for multivariable functions
├── integral/           # Integration methods
├── double_integral/    # Double integration
├── limit/              # Limit calculations
├── taylor_series/      # Taylor series expansions
├── maclaurin_series/   # Maclaurin series (special case of Taylor)
├── fourier_series/     # Fourier series for periodic functions
└── plotter/            # Visualization tools
    ├── plotter_2d.py          # 2D plotting
    ├── plotter_3d.py          # 3D plotting
    ├── vector_field_plotter.py # Vector field visualization
    └── animation_plotter.py    # Animated plots
```

See [STRUCTURE.md](STRUCTURE.md) for detailed documentation.

## Requirements

- Python 3.8 or higher
- NumPy >= 1.20.0
- Matplotlib >= 3.5.0 (for visualization features)

## Installation

### From PyPI (once published)

```bash
pip install calculuskit
```

### From source

```bash
git clone https://github.com/mohamedsajith/calculuskit.git
cd calculuskit
pip install -e .
```

### Development Installation

For development with all testing and linting tools:

```bash
pip install -e ".[dev]"
```

## Quick Start

```python
from calculuskit import Derivative, PartialDerivative, Integral, Limit
from calculuskit import TaylorSeries, MaclaurinSeries, FourierSeries
import math

# Derivative class
df = Derivative(lambda x: x**3)
print(f"f'(2) = {df.at(2)}")  # Output: 12.0
print(f"f'(3) = {df(3)}")     # Can also call directly

# Partial Derivative class
pdg = PartialDerivative(lambda x, y: x**2 + y**2)
print(f"∂g/∂x at (2,3) = {pdg.at((2.0, 3.0), 0)}")  # Output: 4.0
gradient = pdg.gradient_vector((2.0, 3.0))
print(f"∇g at (2,3) = {gradient}")  # Output: [4.0, 6.0]

# Integral class
integral = Integral(lambda x: x**2)
print(f"∫h(x)dx from 0 to 1 = {integral.between(0, 1)}")
avg = integral.average_value(0, 1)
print(f"Average value = {avg}")

# Limit class
lim = Limit(lambda x: (x**2 - 1) / (x - 1))
print(f"lim x→1 = {lim.at(1.0)}")
print(f"Is continuous at 1? {lim.is_continuous(1.0)}")

# Taylor Series class
taylor = TaylorSeries(math.exp, n=10)
print(f"e^1 ≈ {taylor.at(1.0, center=0)}")
print(f"Polynomial: {taylor.polynomial_string(center=0)}")

# Fourier Series class
def square_wave(x):
    return 1 if (x % (2*math.pi)) < math.pi else -1

fourier = FourierSeries(square_wave, period=2*math.pi, n=5)
print(f"Square wave at π/2: {fourier.at(math.pi/2)}")
```

### Visualization

```python
from calculuskit import FunctionPlotter
import math

# Create a plotter for a function
plotter = FunctionPlotter(math.sin, x_range=(-2*math.pi, 2*math.pi))

# 2D plot
plotter.plot(title="Sine Function", color="blue")

# Plot multiple functions
functions = [
    (math.sin, "sin(x)"),
    (math.cos, "cos(x)"),
    (lambda x: math.sin(x) * math.cos(x), "sin(x)cos(x)")
]
plotter.plot_multiple(functions, title="Trigonometric Functions")

# Parametric plot
plotter.parametric_plot(
    lambda t: math.cos(t),  # x(t)
    lambda t: math.sin(t),  # y(t)
    title="Circle"
)

# 3D surface plot
plotter.surface_plot_3d(
    lambda x, y: x**2 + y**2,
    x_range=(-5, 5),
    y_range=(-5, 5),
    title="Paraboloid"
)

# Contour plot
plotter.contour_plot(
    lambda x, y: math.sin(x) * math.cos(y),
    x_range=(-math.pi, math.pi),
    y_range=(-math.pi, math.pi)
)

# Vector field plot
plotter.quiver_plot(
    lambda x, y: -y,  # u component
    lambda x, y: x,   # v component
    x_range=(-3, 3),
    y_range=(-3, 3),
    title="Rotation Field"
)

# Animation: Series approximation
plotter.animate_series_approximation(
    func=math.sin,
    approximation_func=lambda x, n: sum(
        (-1)**k * x**(2*k+1) / math.factorial(2*k+1)
        for k in range(n)
    ),
    max_terms=10,
    title_func=lambda n: f"sin(x) Taylor Series: {n} terms"
)
```

## API Reference

### Class-based API

#### `Derivative(func, h=1e-7, method='central')`

Create a derivative calculator for a function.

**Methods:**
- `at(x)`: Calculate derivative at point x
- `__call__(x)`: Call object as function to get derivative
- `gradient(x, dx, n_points)`: Get derivative values over a range

#### `PartialDerivative(func, h=1e-7)`

Create a partial derivative calculator for multivariable functions.

**Methods:**
- `at(point, var_index)`: Calculate partial derivative
- `gradient_vector(point)`: Get gradient vector (all partial derivatives)
- `jacobian(point)`: Get Jacobian matrix

#### `Integral(func, n=1000, method='simpson')`

Create an integral calculator for a function.

**Methods:**
- `between(a, b)`: Calculate definite integral
- `definite(a, b)`: Alias for between
- `cumulative(a, b, num_points)`: Get cumulative integral values
- `average_value(a, b)`: Get average value over interval

#### `DoubleIntegral(func, n=100, method='simpson')`

Create a double integral calculator for two-variable functions.

**Methods:**
- `over(x_min, x_max, y_min, y_max)`: Calculate double integral over rectangular region

#### `Limit(func, epsilon=1e-10)`

Create a limit calculator for a function.

**Methods:**
- `at(x0, direction='both')`: Calculate limit at point
- `left(x0)`: Calculate left-hand limit
- `right(x0)`: Calculate right-hand limit
- `exists(x0)`: Check if limit exists
- `is_continuous(x0)`: Check if function is continuous
- `as_x_approaches_infinity(direction='positive')`: Calculate limit at infinity

#### `TaylorSeries(func, n=10)`

Create a Taylor series calculator for a function.

**Methods:**
- `at(x, center=0.0)`: Evaluate series at point
- `coefficients(center=0.0)`: Get series coefficients
- `polynomial_string(center=0.0)`: Get string representation
- `error_estimate(x, center=0.0)`: Estimate approximation error

#### `MaclaurinSeries(func, n=10)`

Create a Maclaurin series calculator (Taylor series centered at 0).

**Methods:**
- `at(x)`: Evaluate series at point
- `coefficients()`: Get series coefficients
- `polynomial_string()`: Get string representation
- `error_estimate(x)`: Estimate approximation error

#### `FourierSeries(func, period=2π, n=10)`

Create a Fourier series calculator for periodic functions.

**Methods:**
- `a0()`: Get a0 coefficient (DC component)
- `an(n)`: Get nth cosine coefficient
- `bn(n)`: Get nth sine coefficient
- `at(x)`: Evaluate series at point

#### `FunctionPlotter(func, x_range=(-10, 10), n_points=1000)`

Create a unified plotting interface for visualizing mathematical functions.

**2D Plotting Methods:**
- `plot(...)`: Create a basic 2D line plot
- `plot_multiple(functions, ...)`: Plot multiple functions on the same axes
- `parametric_plot(x_func, y_func, ...)`: Create parametric plots
- `polar_plot(r_func, ...)`: Create polar coordinate plots
- `scatter_data(x_data, y_data, ...)`: Create scatter plots

**3D Plotting Methods:**
- `surface_plot_3d(func, x_range, y_range, ...)`: Create 3D surface plots
- `contour_plot(func, x_range, y_range, ...)`: Create 2D contour plots

**Vector Field Methods:**
- `quiver_plot(u_func, v_func, ...)`: Create vector field plots

**Animation Methods:**
- `animate_series_approximation(func, approximation_func, ...)`: Animate series convergence
- `animate_limit_convergence(sequence_func, ...)`: Animate limit behavior

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/mohamedsajith/calculuskit.git
cd calculuskit

# Install with development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
pytest
```

### Code Quality

This project uses:
- **Ruff**: For linting and formatting
- **mypy**: For static type checking
- **pre-commit**: For automated code quality checks

Run pre-commit manually:
```bash
pre-commit run --all-files
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Mohamed Sajith

## Acknowledgments

- Built with NumPy for efficient numerical computations
- Inspired by classical calculus textbooks and numerical analysis methods
