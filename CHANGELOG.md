# Changelog

All notable changes to CalculusKit will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-10-10

### Added

#### Package Structure
- Created organized folder structure:
  - `core/` - Core calculus operations
  - `analysis/` - Advanced analysis tools
  - `utils/` - Utility functions
  - `visualization/` - Plotting utilities (optional)

#### Core Calculus Operations
- **Derivatives Module** (`core/derivatives.py`):
  - `Derivative` class for single-variable derivatives
  - `PartialDerivative` class for multivariable functions
  - `gradient()` method for derivative values over ranges
  - `gradient_vector()` method for full gradients
  - `jacobian()` method for Jacobian matrices

- **Integrals Module** (`core/integrals.py`):
  - `Integral` class with cumulative integration support
  - `DoubleIntegral` class for 2D integration
  - `average_value()` method for function averages
  - `cumulative()` method for cumulative integral values

- **Limits Module** (`core/limits.py`):
  - `Limit` class with enhanced methods
  - `exists()` method to check limit existence
  - `is_continuous()` method for continuity checking
  - `as_x_approaches_infinity()` for limits at infinity

- **Series Module** (`core/series.py`):
  - `TaylorSeries` class with coefficient extraction
  - `MaclaurinSeries` class (Taylor at 0)
  - `FourierSeries` class for periodic functions
  - `polynomial_string()` for string representations
  - `error_estimate()` for approximation errors

#### Advanced Analysis Tools
- **Optimization Module** (`analysis/optimization.py`):
  - `find_critical_points()` - Locate derivative zeros
  - `find_extrema()` - Find maxima and minima
  - `gradient_descent()` - Optimization algorithm

- **Curves Module** (`analysis/curves.py`):
  - `arc_length()` - Calculate curve length
  - `curvature()` - Compute curvature at points
  - `surface_area_of_revolution()` - Surface area calculations

#### Utilities
- **Numerical Utilities** (`utils/numerical.py`):
  - `is_close()` - Float comparison
  - `linspace()` - Linear spacing
  - `numerical_stability_check()` - Stability verification

- **Validators** (`utils/validators.py`):
  - `validate_function()` - Callable checking
  - `validate_bounds()` - Bounds validation
  - `validate_point()` - Point validation

#### Visualization (Optional)
- **Plotters Module** (`visualization/plotters.py`):
  - `plot_function()` - Basic function plotting
  - `plot_derivative()` - Function and derivative plots
  - `plot_integral()` - Integral with shaded area
  - `plot_tangent_line()` - Tangent line visualization
  - Requires: matplotlib (optional dependency)

#### Documentation
- `STRUCTURE.md` - Detailed package structure documentation
- `QUICK_REFERENCE.md` - Quick reference guide
- `PUBLISHING.md` - PyPI publishing instructions
- `SUMMARY.md` - Implementation summary
- Enhanced `README.md` with new features

#### Development Tools
- Pre-commit hooks configured:
  - Ruff for linting and formatting
  - mypy for type checking
  - Bandit for security scanning
- Full type hints throughout codebase
- Comprehensive docstrings with examples

### Changed
- Reorganized package into logical sub-packages
- All previous imports still work (backward compatible)
- Enhanced class methods for better usability

### Technical Details
- Python 3.9+ required
- NumPy 1.20.0+ required
- Matplotlib optional (for visualization)
- Full type checking support
- PEP 517/518 compliant build system

## [Unreleased]

### Planned Features
- Symbolic differentiation support
- More optimization algorithms
- Additional numerical methods
- 3D plotting capabilities
- Interactive Jupyter widgets
- Performance optimizations
- More comprehensive test suite

---

## Version History

- **0.1.0** (2025-10-10): Initial release with structured package layout

[0.1.0]: https://github.com/mohamedsajith/calculuskit/releases/tag/v0.1.0
