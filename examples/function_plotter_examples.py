"""Examples demonstrating the FunctionPlotter class.

This module contains various examples showing how to use the FunctionPlotter
class for visualizing mathematical functions.
"""

import math

from calculuskit.derivative import Derivative
from calculuskit.plotter import FunctionPlotter


def example_basic_plot() -> None:
    """Example 1: Basic function plot."""
    print("Example 1: Basic Quadratic Function Plot")
    print("-" * 50)

    # Define a simple quadratic function
    def f(x: float) -> float:
        return x**2

    # Create plotter and plot
    plotter = FunctionPlotter(f, x_range=(-5, 5))
    plotter.plot(
        title="Quadratic Function: f(x) = x²",
        xlabel="x",
        ylabel="f(x)",
        color="blue",
        grid=True,
    )
    print("Displayed quadratic function plot\n")


def example_trigonometric_functions() -> None:
    """Example 2: Plot multiple trigonometric functions."""
    print("Example 2: Trigonometric Functions")
    print("-" * 50)

    # Define trigonometric functions
    def sin_func(x: float) -> float:
        return math.sin(x)

    def cos_func(x: float) -> float:
        return math.cos(x)

    def tan_func(x: float) -> float:
        return math.tan(x)

    # Plot multiple functions together
    functions = [
        (sin_func, "sin(x)"),
        (cos_func, "cos(x)"),
    ]

    plotter = FunctionPlotter(sin_func, x_range=(0, 2 * math.pi))
    plotter.plot_multiple(
        functions,
        title="Sine and Cosine Functions",
        xlabel="x (radians)",
        ylabel="y",
        colors=["red", "blue"],
    )
    print("Displayed sine and cosine functions\n")


def example_function_with_derivative() -> None:
    """Example 3: Plot function with its derivative."""
    print("Example 3: Function with Derivative")
    print("-" * 50)

    # Define a cubic function
    def f(x: float) -> float:
        return x**3 - 3 * x**2 + 2

    # Define its derivative
    def df(x: float) -> float:
        return 3 * x**2 - 6 * x

    # Or use the Derivative class
    derivative = Derivative(f)

    plotter = FunctionPlotter(f, x_range=(-2, 4))
    plotter.plot_with_derivative(
        derivative,
        title="Cubic Function and Its Derivative",
        func_label="f(x) = x³ - 3x² + 2",
        deriv_label="f'(x) = 3x² - 6x",
        func_color="blue",
        deriv_color="red",
    )
    print("Displayed function with its derivative\n")


def example_exponential_and_logarithmic() -> None:
    """Example 4: Exponential and logarithmic functions."""
    print("Example 4: Exponential and Logarithmic Functions")
    print("-" * 50)

    def exp_func(x: float) -> float:
        return math.exp(x)

    def log_func(x: float) -> float:
        return math.log(x)

    # Plot exponential function
    plotter_exp = FunctionPlotter(exp_func, x_range=(-2, 3))
    plotter_exp.plot(
        title="Exponential Function: f(x) = e^x",
        xlabel="x",
        ylabel="f(x)",
        color="green",
    )

    # Plot logarithmic function
    plotter_log = FunctionPlotter(log_func, x_range=(0.1, 10))
    plotter_log.plot(
        title="Natural Logarithm: f(x) = ln(x)",
        xlabel="x",
        ylabel="f(x)",
        color="orange",
    )
    print("Displayed exponential and logarithmic functions\n")


def example_parametric_curves() -> None:
    """Example 5: Parametric curve plotting."""
    print("Example 5: Parametric Curves")
    print("-" * 50)

    # Circle
    def x_circle(t: float) -> float:
        return math.cos(t)

    def y_circle(t: float) -> float:
        return math.sin(t)

    plotter = FunctionPlotter(lambda x: x)
    plotter.plot_parametric(
        x_circle,
        y_circle,
        t_range=(0, 2 * math.pi),
        title="Unit Circle",
        color="purple",
    )

    # Lissajous curve
    def x_lissajous(t: float) -> float:
        return math.sin(3 * t)

    def y_lissajous(t: float) -> float:
        return math.cos(2 * t)

    plotter.plot_parametric(
        x_lissajous,
        y_lissajous,
        t_range=(0, 2 * math.pi),
        title="Lissajous Curve",
        color="red",
    )
    print("Displayed parametric curves\n")


def example_polar_plots() -> None:
    """Example 6: Polar coordinate plots."""
    print("Example 6: Polar Plots")
    print("-" * 50)

    # Cardioid
    def cardioid(theta: float) -> float:
        return 1 + math.cos(theta)

    plotter = FunctionPlotter(lambda x: x)
    plotter.plot_polar(
        cardioid,
        theta_range=(0, 2 * math.pi),
        title="Cardioid: r = 1 + cos(θ)",
        color="magenta",
    )

    # Rose curve
    def rose(theta: float) -> float:
        return math.cos(4 * theta)

    plotter.plot_polar(
        rose,
        theta_range=(0, 2 * math.pi),
        title="Rose Curve: r = cos(4θ)",
        color="green",
    )

    # Spiral
    def spiral(theta: float) -> float:
        return theta / (2 * math.pi)

    plotter.plot_polar(
        spiral,
        theta_range=(0, 6 * math.pi),
        title="Archimedean Spiral: r = θ/(2π)",
        color="blue",
    )
    print("Displayed polar plots\n")


def example_scatter_plots() -> None:
    """Example 7: Scatter plots with data."""
    print("Example 7: Scatter Plots")
    print("-" * 50)

    # Simulated experimental data
    x_data = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    y_data = [0.1, 0.9, 4.2, 8.8, 16.1, 25.2]  # Approximately y = x^2

    plotter = FunctionPlotter(lambda x: x)

    # Scatter plot with linear fit
    plotter.scatter_plot(
        x_data,
        y_data,
        title="Data Points with Linear Fit",
        xlabel="x",
        ylabel="y",
        color="blue",
        show_fit=True,
        fit_degree=1,
    )

    # Scatter plot with quadratic fit
    plotter.scatter_plot(
        x_data,
        y_data,
        title="Data Points with Quadratic Fit",
        xlabel="x",
        ylabel="y",
        color="red",
        marker="s",
        show_fit=True,
        fit_degree=2,
    )
    print("Displayed scatter plots with curve fitting\n")


def example_custom_styling() -> None:
    """Example 8: Custom styling options."""
    print("Example 8: Custom Styling")
    print("-" * 50)

    def f(x: float) -> float:
        return math.sin(x) * math.exp(-x / 10)

    plotter = FunctionPlotter(f, x_range=(0, 20))
    plotter.plot(
        title="Damped Sine Wave",
        xlabel="Time (s)",
        ylabel="Amplitude",
        color="darkblue",
        linestyle="--",
        linewidth=2.5,
        grid=True,
        figsize=(12, 6),
    )
    print("Displayed custom styled plot\n")


def example_piecewise_function() -> None:
    """Example 9: Piecewise function."""
    print("Example 9: Piecewise Function")
    print("-" * 50)

    def piecewise(x: float) -> float:
        if x < -2:
            return -1
        elif x < 2:
            return x**2
        else:
            return 4 + (x - 2)

    plotter = FunctionPlotter(piecewise, x_range=(-5, 5), n_points=2000)
    plotter.plot(
        title="Piecewise Function",
        xlabel="x",
        ylabel="f(x)",
        color="purple",
        linewidth=2,
    )
    print("Displayed piecewise function\n")


def example_comparing_polynomial_degrees() -> None:
    """Example 10: Compare polynomials of different degrees."""
    print("Example 10: Comparing Polynomial Degrees")
    print("-" * 50)

    def linear(x: float) -> float:
        return x

    def quadratic(x: float) -> float:
        return x**2

    def cubic(x: float) -> float:
        return x**3

    def quartic(x: float) -> float:
        return x**4

    functions = [
        (linear, "x"),
        (quadratic, "x²"),
        (cubic, "x³"),
        (quartic, "x⁴"),
    ]

    plotter = FunctionPlotter(linear, x_range=(-2, 2), n_points=500)
    plotter.plot_multiple(
        functions,
        title="Polynomial Functions Comparison",
        xlabel="x",
        ylabel="y",
        colors=["blue", "green", "red", "purple"],
    )
    print("Displayed polynomial comparison\n")


def example_save_plot_to_file() -> None:
    """Example 11: Save plots to files."""
    print("Example 11: Saving Plots to Files")
    print("-" * 50)

    def f(x: float) -> float:
        return math.sin(x)

    plotter = FunctionPlotter(f, x_range=(0, 2 * math.pi))

    # Save without displaying
    plotter.plot(
        title="Sine Wave",
        show=False,
        save_path="sine_wave.png",
    )
    print("Plot saved to 'sine_wave.png'\n")


def example_integration_with_derivative_class() -> None:
    """Example 12: Integration with CalculusKit's Derivative class."""
    print("Example 12: Integration with Derivative Class")
    print("-" * 50)

    # Define a function
    def f(x: float) -> float:
        return x**4 - 4 * x**3 + 6 * x**2 - 4 * x + 1

    # Create a derivative calculator
    derivative = Derivative(f, method="central")

    # Plot the function and its derivative
    plotter = FunctionPlotter(f, x_range=(-1, 5))
    plotter.plot_with_derivative(
        derivative,
        title="Polynomial and Its Derivative",
        func_label="f(x) = x⁴ - 4x³ + 6x² - 4x + 1",
        deriv_label="f'(x)",
        func_color="blue",
        deriv_color="red",
    )

    # Plot gradient visualization
    x_vals, deriv_vals = derivative.gradient(x=2.0, dx=2.0, n_points=100)

    plotter_deriv = FunctionPlotter(derivative, x_range=(0, 4))
    plotter_deriv.plot(
        title="Derivative Gradient Around x=2",
        xlabel="x",
        ylabel="f'(x)",
        color="green",
    )
    print("Displayed function with derivative using Derivative class\n")


def example_mathematical_constants() -> None:
    """Example 13: Functions involving mathematical constants."""
    print("Example 13: Mathematical Constants")
    print("-" * 50)

    # Golden ratio spiral
    phi = (1 + math.sqrt(5)) / 2  # Golden ratio

    def golden_spiral(theta: float) -> float:
        return phi ** (2 * theta / math.pi)

    plotter = FunctionPlotter(lambda x: x)
    plotter.plot_polar(
        golden_spiral,
        theta_range=(0, 4 * math.pi),
        title="Golden Ratio Spiral",
        color="gold",
    )

    # Euler's number
    def euler_func(x: float) -> float:
        return math.e**x

    plotter_euler = FunctionPlotter(euler_func, x_range=(-2, 2))
    plotter_euler.plot(
        title="Exponential Growth: f(x) = e^x",
        color="red",
    )
    print("Displayed functions with mathematical constants\n")


def example_contour_plots() -> None:
    """Example 14: Contour plots for multivariable functions."""
    print("Example 14: Contour Plots for Multivariable Functions")
    print("-" * 50)

    # Paraboloid: z = x^2 + y^2
    def paraboloid(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = FunctionPlotter(lambda x: x)
    plotter.contour_plot(
        paraboloid,
        x_range=(-5, 5),
        y_range=(-5, 5),
        title="Paraboloid: z = x² + y²",
        colormap="viridis",
        levels=20,
    )

    # Saddle point: z = x^2 - y^2
    def saddle(x: float, y: float) -> float:
        return x**2 - y**2

    plotter.contour_plot(
        saddle,
        x_range=(-3, 3),
        y_range=(-3, 3),
        title="Saddle Point: z = x² - y²",
        colormap="coolwarm",
        levels=30,
    )

    # Gaussian function
    def gaussian(x: float, y: float) -> float:
        return math.exp(-(x**2 + y**2))

    plotter.contour_plot(
        gaussian,
        x_range=(-3, 3),
        y_range=(-3, 3),
        title="2D Gaussian: z = e^(-(x² + y²))",
        colormap="hot",
        levels=25,
    )

    # Trigonometric function
    def trig_2d(x: float, y: float) -> float:
        return math.sin(x) * math.cos(y)

    plotter.contour_plot(
        trig_2d,
        x_range=(-math.pi, math.pi),
        y_range=(-math.pi, math.pi),
        title="z = sin(x) · cos(y)",
        colormap="RdBu",
        levels=20,
    )

    print("Displayed contour plots\n")


def example_contour_line_plots() -> None:
    """Example 15: Line contour plots (not filled)."""
    print("Example 15: Line Contour Plots")
    print("-" * 50)

    # Ripple function
    def ripple(x: float, y: float) -> float:
        r = math.sqrt(x**2 + y**2)
        if r == 0:
            return 1.0
        return math.sin(r) / r

    plotter = FunctionPlotter(lambda x: x)
    plotter.contour_plot(
        ripple,
        x_range=(-10, 10),
        y_range=(-10, 10),
        title="Ripple Function: z = sin(r)/r",
        filled=False,
        levels=15,
    )
    print("Displayed line contour plot\n")


def example_3d_surface_plots() -> None:
    """Example 16: 3D surface plots."""
    print("Example 16: 3D Surface Plots")
    print("-" * 50)

    # Paraboloid
    def paraboloid(x: float, y: float) -> float:
        return x**2 + y**2

    plotter = FunctionPlotter(lambda x: x)
    plotter.surface_plot_3d(
        paraboloid,
        x_range=(-5, 5),
        y_range=(-5, 5),
        title="3D Paraboloid: z = x² + y²",
        colormap="viridis",
        elevation=30,
        azimuth=45,
    )

    # Saddle point
    def saddle(x: float, y: float) -> float:
        return x**2 - y**2

    plotter.surface_plot_3d(
        saddle,
        x_range=(-3, 3),
        y_range=(-3, 3),
        title="3D Saddle Point: z = x² - y²",
        colormap="coolwarm",
        elevation=20,
        azimuth=60,
    )

    # Wave function
    def wave(x: float, y: float) -> float:
        return math.sin(math.sqrt(x**2 + y**2))

    plotter.surface_plot_3d(
        wave,
        x_range=(-5, 5),
        y_range=(-5, 5),
        title="Wave Function: z = sin(√(x² + y²))",
        colormap="plasma",
        show_contour=True,
    )

    print("Displayed 3D surface plots\n")


def example_multivariable_combined() -> None:
    """Example 17: Combined contour and 3D visualization."""
    print("Example 17: Combined Contour and 3D Surface Plots")
    print("-" * 50)

    # Mexican hat function
    def mexican_hat(x: float, y: float) -> float:
        r_squared = x**2 + y**2
        return (1 - r_squared) * math.exp(-r_squared / 2)

    plotter = FunctionPlotter(lambda x: x)

    # Show contour plot
    plotter.contour_plot(
        mexican_hat,
        x_range=(-3, 3),
        y_range=(-3, 3),
        title="Mexican Hat (Contour): z = (1 - r²)e^(-r²/2)",
        colormap="seismic",
        levels=30,
    )

    # Show 3D surface
    plotter.surface_plot_3d(
        mexican_hat,
        x_range=(-3, 3),
        y_range=(-3, 3),
        title="Mexican Hat (3D): z = (1 - r²)e^(-r²/2)",
        colormap="seismic",
        show_contour=True,
        elevation=25,
        azimuth=135,
    )

    print("Displayed combined visualization\n")


def main() -> None:
    """Run all examples."""
    print("\n" + "=" * 60)
    print("CalculusKit Function Plotter Examples")
    print("=" * 60 + "\n")

    examples = [
        ("Basic Plot", example_basic_plot),
        ("Trigonometric Functions", example_trigonometric_functions),
        ("Function with Derivative", example_function_with_derivative),
        ("Exponential and Logarithmic", example_exponential_and_logarithmic),
        ("Parametric Curves", example_parametric_curves),
        ("Polar Plots", example_polar_plots),
        ("Scatter Plots", example_scatter_plots),
        ("Custom Styling", example_custom_styling),
        ("Piecewise Function", example_piecewise_function),
        ("Polynomial Comparison", example_comparing_polynomial_degrees),
        ("Save to File", example_save_plot_to_file),
        ("Derivative Class Integration", example_integration_with_derivative_class),
        ("Mathematical Constants", example_mathematical_constants),
        ("Contour Plots", example_contour_plots),
        ("Line Contour Plots", example_contour_line_plots),
        ("3D Surface Plots", example_3d_surface_plots),
        ("Combined Multivariable Plots", example_multivariable_combined),
    ]

    print("Available examples:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"  {i}. {name}")

    print("\nRunning all examples...")
    print("Close each plot window to see the next example.\n")

    for name, example_func in examples:
        try:
            example_func()
        except Exception as e:
            print(f"Error in {name}: {e}\n")

    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
