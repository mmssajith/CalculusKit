# CalculusKit Package Structure

## Overview

CalculusKit is organized into four main sub-packages, each serving a specific purpose:

```
calculuskit/
├── __init__.py              # Main package entry point
├── core/                    # Core calculus operations
│   ├── __init__.py
│   ├── derivatives.py       # Derivative calculations
│   ├── integrals.py         # Integration operations
│   ├── limits.py            # Limit calculations
│   └── series.py            # Series expansions
├── analysis/                # Advanced analysis tools
│   ├── __init__.py
│   ├── optimization.py      # Critical points, extrema, gradient descent
│   └── curves.py            # Arc length, curvature, surface area
├── utils/                   # Utility functions
│   ├── __init__.py
│   ├── numerical.py         # Numerical utilities
│   └── validators.py        # Input validation
└── visualization/           # Plotting utilities (optional)
    ├── __init__.py
    └── plotters.py          # Visualization functions
```

## Package Descriptions

### 1. Core (`calculuskit.core`)

Contains the fundamental calculus operations with both function-based and class-based APIs.

#### Modules:
- **derivatives.py**: Single and multi-variable derivatives
  - Functions: `derivative()`, `partial_derivative()`
  - Classes: `Derivative`, `PartialDerivative`

- **integrals.py**: Integration operations
  - Functions: `integrate()`, `definite_integral()`
  - Classes: `Integral`, `DoubleIntegral`

- **limits.py**: Limit calculations
  - Functions: `limit()`
  - Classes: `Limit`

- **series.py**: Series expansions
  - Functions: `taylor_series()`, `maclaurin_series()`
  - Classes: `TaylorSeries`, `MaclaurinSeries`, `FourierSeries`

### 2. Analysis (`calculuskit.analysis`)

Advanced mathematical analysis tools built on top of core operations.

#### Modules:
- **optimization.py**:
  - `find_critical_points()`: Find points where derivative is zero
  - `find_extrema()`: Find local maxima and minima
  - `gradient_descent()`: Optimization using gradient descent

- **curves.py**:
  - `arc_length()`: Calculate curve length
  - `curvature()`: Calculate curvature at a point
  - `surface_area_of_revolution()`: Surface area when curve rotates

### 3. Utils (`calculuskit.utils`)

Utility functions for numerical operations and validation.

#### Modules:
- **numerical.py**:
  - `is_close()`: Compare floating point numbers
  - `linspace()`: Generate linearly spaced values
  - `numerical_stability_check()`: Check function stability

- **validators.py**:
  - `validate_function()`: Ensure object is callable
  - `validate_bounds()`: Check integration bounds
  - `validate_point()`: Validate n-dimensional points

### 4. Visualization (`calculuskit.visualization`)

Plotting utilities for visualizing calculus operations.

**Note**: Requires matplotlib (install with `pip install matplotlib`)

#### Modules:
- **plotters.py**:
  - `plot_function()`: Plot a function
  - `plot_derivative()`: Plot function and its derivative
  - `plot_integral()`: Plot with shaded area
  - `plot_tangent_line()`: Plot tangent line at a point

## Usage Examples

### Importing from Sub-packages

```python
import calculuskit as ck

# All core functions/classes are available directly
df = ck.Derivative(lambda x: x**2)
result = ck.derivative(lambda x: x**2, 3.0)

# Analysis tools
critical_pts = ck.find_critical_points(lambda x: x**3 - 3*x, -3, 3)
extrema = ck.find_extrema(lambda x: x**3 - 3*x, -3, 3)
arc = ck.arc_length(lambda x: x**2, 0, 1)

# Utilities
ck.validate_bounds(0, 1)
stable = ck.numerical_stability_check(lambda x: 1/x, 0.5)

# Visualization (if matplotlib installed)
ck.plot_function(lambda x: x**2, -5, 5)
```

### Direct Sub-package Imports

```python
# Import specific sub-packages
from calculuskit.core import Derivative, Integral
from calculuskit.analysis import find_critical_points, curvature
from calculuskit.utils import validate_function
from calculuskit.visualization import plot_derivative

# Use them
df = Derivative(lambda x: x**3)
integral = Integral(lambda x: x**2)
critical = find_critical_points(lambda x: x**2 - 4*x, 0, 5)
```

### Module-level Imports

```python
# Import entire modules
from calculuskit import core, analysis, utils

# Access through modules
df = core.Derivative(lambda x: x**2)
extrema = analysis.find_extrema(lambda x: x**3, -2, 2)
utils.validate_bounds(0, 1)
```

## Design Principles

1. **Separation of Concerns**: Each sub-package has a clear, distinct purpose
2. **Progressive Complexity**: Core → Analysis → Visualization
3. **Optional Dependencies**: Visualization requires matplotlib but core doesn't
4. **Dual API**: Function-based (simple) and class-based (powerful) approaches
5. **Type Safety**: Full type hints throughout the codebase

## Adding New Functionality

### To add a new core operation:
1. Add implementation to appropriate file in `core/`
2. Export from `core/__init__.py`
3. Re-export from main `__init__.py`

### To add analysis tools:
1. Create function in appropriate file in `analysis/`
2. Export from `analysis/__init__.py`
3. Re-export from main `__init__.py`

### To add utilities:
1. Add to appropriate file in `utils/`
2. Export from `utils/__init__.py`
3. Optionally re-export from main `__init__.py`

## Benefits of This Structure

1. **Modularity**: Easy to import only what you need
2. **Extensibility**: Clear where to add new features
3. **Maintainability**: Related code is grouped together
4. **Testing**: Each module can be tested independently
5. **Documentation**: Structure mirrors functionality
6. **Performance**: Import only required sub-packages

## Backward Compatibility

All previous imports still work:
```python
import calculuskit as ck

# These all work exactly as before
ck.derivative(func, x)
ck.Derivative(func)
ck.integrate(func, a, b)
ck.Integral(func)
# etc.
```

No code changes needed when upgrading!
