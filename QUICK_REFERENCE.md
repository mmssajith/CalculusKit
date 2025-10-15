# CalculusKit Quick Reference

## Installation
```bash
pip install calculuskit
```

## Import
```python
import calculuskit as ck
```

## Quick Examples

### Derivatives
```python
# Function API
ck.derivative(lambda x: x**2, 3.0)  # → 6.0

# Class API
df = ck.Derivative(lambda x: x**3)
df.at(2)  # → 12.0
df(2)     # → 12.0 (callable)
```

### Partial Derivatives
```python
# Function API
ck.partial_derivative(lambda x, y: x**2 + y**2, (2.0, 3.0), 0)  # → 4.0

# Class API
pd = ck.PartialDerivative(lambda x, y: x**2 + y**2)
pd.at((2.0, 3.0), 0)           # → 4.0
pd.gradient_vector((2.0, 3.0)) # → [4.0, 6.0]
```

### Integration
```python
# Function API
ck.integrate(lambda x: x**2, 0, 1)  # → 0.333...

# Class API
integral = ck.Integral(lambda x: x**2)
integral.between(0, 1)        # → 0.333...
integral.average_value(0, 1)  # → 0.333...
```

### Double Integration
```python
dbl = ck.DoubleIntegral(lambda x, y: x * y)
dbl.over(0, 1, 0, 1)  # → 0.25
```

### Limits
```python
# Function API
ck.limit(lambda x: (x**2 - 1) / (x - 1), 1.0)  # → 2.0

# Class API
lim = ck.Limit(lambda x: (x**2 - 1) / (x - 1))
lim.at(1.0)              # → 2.0
lim.left(1.0)            # Left-hand limit
lim.right(1.0)           # Right-hand limit
lim.exists(1.0)          # → True
lim.is_continuous(1.0)   # → False (discontinuity)
```

### Taylor Series
```python
import math

# Function API
ck.taylor_series(math.sin, 0, 0.5, n=10)  # → 0.479...

# Class API
taylor = ck.TaylorSeries(math.sin, n=10)
taylor.at(0.5, center=0)         # → 0.479...
taylor.polynomial_string(center=0)  # String representation
taylor.error_estimate(0.5)       # Approximation error
```

### Maclaurin Series
```python
import math

# Function API
ck.maclaurin_series(math.cos, 1.0, n=10)  # → 0.540...

# Class API
maclaurin = ck.MaclaurinSeries(math.cos, n=10)
maclaurin.at(1.0)           # → 0.540...
maclaurin.coefficients()    # List of coefficients
```

### Fourier Series
```python
import math

def square_wave(x):
    return 1 if (x % (2*math.pi)) < math.pi else -1

fourier = ck.FourierSeries(square_wave, period=2*math.pi, n=10)
fourier.a0()                # DC component
fourier.an(1)               # 1st cosine coefficient
fourier.bn(1)               # 1st sine coefficient
fourier.at(math.pi/2)       # Evaluate at π/2
```

### Function Plotting
```python
import math

plotter = ck.FunctionPlotter(math.sin, x_range=(-10, 10))
plotter.plot(title="Sine Function")
plotter.plot_with_derivative(lambda x: math.cos(x))
plotter.contour_plot(lambda x, y: x**2 + y**2)
plotter.surface_plot_3d(lambda x, y: x**2 + y**2)
```

### Vector Fields (Quiver Plots)
```python
# Gradient field
def u(x, y): return 2*x
def v(x, y): return 2*y

plotter = ck.FunctionPlotter(lambda x: x)
plotter.quiver_plot(
    u, v,
    x_range=(-5, 5),
    y_range=(-5, 5),
    show_magnitude=True  # Color by magnitude
)
```

### Animations
```python
import math

# Animate Taylor series convergence
def f(x): return math.exp(x)
def taylor_approx(x, n):
    return sum(x**k / math.factorial(k) for k in range(n+1))

plotter = ck.FunctionPlotter(f, x_range=(-2, 2))
anim = plotter.animate_series_approximation(
    f, taylor_approx,
    max_terms=15,
    title_func=lambda n: f"Taylor Series: {n} terms"
)

# Animate limit convergence
plotter = ck.FunctionPlotter(lambda x: x)
anim = plotter.animate_limit_convergence(
    lambda n: 1/n,
    limit_value=0.0,
    max_n=50
)
```

## Method Options

### Derivative Methods
```python
ck.Derivative(func, method='central')  # 'forward', 'backward', 'central'
```

### Integration Methods
```python
ck.Integral(func, method='simpson')  # 'trapezoidal', 'simpson', 'midpoint'
```

### Limit Directions
```python
lim.at(x0, direction='both')  # 'left', 'right', 'both'
```

## All Available Functions

### Functions
- `derivative(func, x, h, method)`
- `partial_derivative(func, point, var_index, h)`
- `integrate(func, a, b, n, method)`
- `definite_integral(func, a, b, **kwargs)`
- `limit(func, x0, direction, epsilon)`
- `taylor_series(func, x0, x, n)`
- `maclaurin_series(func, x, n)`

### Classes
- `Derivative(func, h, method)`
- `PartialDerivative(func, h)`
- `Integral(func, n, method)`
- `DoubleIntegral(func, n, method)`
- `Limit(func, epsilon)`
- `TaylorSeries(func, n)`
- `MaclaurinSeries(func, n)`
- `FourierSeries(func, period, n)`
- `FunctionPlotter(func, x_range, n_points)`

### Plotting Methods
- `plot()` - Basic 2D function plot
- `plot_with_derivative()` - Plot function with derivative
- `plot_multiple()` - Multiple functions on same axes
- `plot_parametric()` - Parametric curves
- `plot_polar()` - Polar coordinate plots
- `scatter_plot()` - Scatter plots with optional curve fitting
- `contour_plot()` - 2D contour plots for f(x,y)
- `surface_plot_3d()` - 3D surface plots for f(x,y)
- `quiver_plot()` - Vector field (quiver) plots
- `animate_series_approximation()` - Animate series convergence
- `animate_limit_convergence()` - Animate limit convergence

## Tips

1. **Use classes for repeated calculations** on the same function
2. **Use functions for one-off calculations**
3. **Increase `n` for higher accuracy** (at cost of performance)
4. **Check numerical stability** for complex functions
5. **Use appropriate methods** for your use case:
   - Central difference for derivatives (most accurate)
   - Simpson's rule for integration (good balance)

## Common Patterns

### Finding Critical Points
```python
df = ck.Derivative(lambda x: x**3 - 3*x)
# Find where derivative ≈ 0
for x in range(-3, 4):
    if abs(df(x)) < 0.1:
        print(f"Critical point near x={x}")
```

### Checking Continuity
```python
lim = ck.Limit(your_function)
for x in suspicious_points:
    if not lim.is_continuous(x):
        print(f"Discontinuous at x={x}")
```

### Computing Arc Length
```python
import math
df = ck.Derivative(your_curve)
arc_integrand = lambda x: math.sqrt(1 + df(x)**2)
arc_length = ck.integrate(arc_integrand, a, b)
```

## Getting Help

```python
help(ck.Derivative)
help(ck.integrate)
```

Visit: https://github.com/mohamedsajith/calculuskit
