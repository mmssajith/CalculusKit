# CalculusKit Examples

This directory contains comprehensive examples demonstrating the features of CalculusKit.

## Files

### Basic Examples

- **`basic_derivatives.py`** - Introduction to derivatives
  - Simple polynomial derivatives
  - Different differentiation methods (forward, backward, central)
  - Exponential and trigonometric functions
  - Gradient calculations
  - Using derivative objects as callables

- **`basic_integrals.py`** - Introduction to integrals
  - Definite integrals
  - Different integration methods (trapezoidal, Simpson's, midpoint)
  - Cumulative integrals
  - Average value of functions
  - Area under curves

- **`basic_limits.py`** - Introduction to limits
  - Simple limits
  - One-sided limits (left and right)
  - Continuity testing
  - Famous limits (sin(x)/x, etc.)
  - Limits at infinity

- **`taylor_series_examples.py`** - Taylor series expansions
  - Taylor series for common functions (e^x, sin(x), cos(x))
  - Different center points
  - Extracting coefficients
  - Polynomial string representation
  - Error estimation

- **`function_plotter_examples.py`** - Function plotting and visualization
  - Basic function plots
  - Plotting functions with derivatives
  - Multiple functions on same axes
  - Parametric curves
  - Polar coordinate plots
  - Scatter plots with curve fitting
  - Custom styling and formatting

- **`vector_field_examples.py`** - Vector field (quiver plot) visualization
  - Gradient fields
  - Rotation and vortex fields
  - Radial fields
  - Physical field visualizations (electric dipole, shear flow)
  - Magnitude-based coloring
  - Vector normalization
  - Custom arrow density

- **`animation_examples.py`** - Animated series and limit convergence
  - Taylor series convergence (e^x, sin(x), cos(x))
  - Fourier series approximation (square wave)
  - Limit convergence visualization
  - Famous limits (convergence to e)
  - Alternating sequences
  - Squeeze theorem examples
  - Custom animation timing and styling

### Advanced Examples

- **`advanced_examples.py`** - Complex applications combining multiple features
  - Fundamental Theorem of Calculus verification
  - Finding extrema (maxima/minima)
  - Arc length calculations
  - Rate of change analysis
  - Physics applications (work and energy)
  - Related rates problems
  - Numerical vs analytical comparisons

## Running the Examples

Each file can be run independently:

```bash
# Run basic derivative examples
python examples/basic_derivatives.py

# Run basic integral examples
python examples/basic_integrals.py

# Run limit examples
python examples/basic_limits.py

# Run Taylor series examples
python examples/taylor_series_examples.py

# Run function plotter examples
python examples/function_plotter_examples.py

# Run vector field examples
python examples/vector_field_examples.py

# Run animation examples
python examples/animation_examples.py

# Run advanced examples
python examples/advanced_examples.py
```

## Requirements

All examples require CalculusKit to be installed:

```bash
pip install calculuskit
```

Or if running from the repository:

```bash
pip install -e .
```

**Note:** The `function_plotter_examples.py` requires matplotlib to be installed, which is included as a dependency when you install CalculusKit.

## Learning Path

For beginners, we recommend following this order:

1. **Start with derivatives**: `basic_derivatives.py`
   - Understand how to create Derivative objects
   - Learn about different differentiation methods
   - See practical applications

2. **Move to integrals**: `basic_integrals.py`
   - Learn about definite integrals
   - Compare integration methods
   - Understand cumulative integrals

3. **Explore limits**: `basic_limits.py`
   - Understand limit concepts
   - Learn about continuity
   - Work with one-sided limits

4. **Study Taylor series**: `taylor_series_examples.py`
   - Understand series expansions
   - Learn about convergence and error
   - Approximate complex functions

5. **Visualize with plots**: `function_plotter_examples.py`
   - Learn to visualize functions
   - Plot derivatives and integrals
   - Create parametric and polar plots

6. **Explore vector fields**: `vector_field_examples.py`
   - Visualize gradient fields
   - Understand physical vector fields
   - Create quiver plots

7. **Watch animations**: `animation_examples.py`
   - See series convergence in action
   - Visualize limit behavior
   - Understand approximation dynamics

8. **Apply advanced concepts**: `advanced_examples.py`
   - Combine multiple concepts
   - See real-world applications
   - Understand relationships between calculus operations

## Example Output

When you run the examples, you'll see formatted output showing:
- The problem being solved
- Numerical results from CalculusKit
- Expected analytical results (when available)
- Error analysis comparing numerical vs analytical solutions

## Contributing

Have an interesting example? Feel free to contribute! Examples should:
- Be well-documented with docstrings
- Include expected results for verification
- Show practical applications
- Follow the existing code style

## Need Help?

If you're having trouble with any examples:
1. Check that CalculusKit is properly installed
2. Ensure you're using Python 3.9 or higher
3. Verify all dependencies are installed (numpy)
4. Review the main CalculusKit documentation
